#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from ui_main_window import Ui_MainWindow
import rc_ex_tr
from control_types import ExerciseType, PositionType, SwitchType
from detection_exercises import *


# In[ ]:


import sys
from PySide2 import QtCore, QtGui, QtWidgets


# In[ ]:


import cv2
import mediapipe as mp
import numpy as np
import math 


# In[ ]:


import qimage2ndarray


# In[ ]:


class VideoDetectionThread(QtCore.QThread):
    changeCount = QtCore.Signal(int)
    changeExercise = QtCore.Signal(int)
    changePixmap = QtCore.Signal(QtGui.QImage)
    
    def __init__(self, exercise_list):
        super(VideoDetectionThread, self).__init__()
        
        self.exercise_list = exercise_list
        self.exercise_index = 0
        
        self.counter = 0
        
        self.detection_show = False
        
        self.video = cv2.VideoCapture()
        
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        
        
    def run(self):
        sec = 0

        sw_type = None

        current_position = None
        first_position = None
        second_position = None

        positions = [PositionType.FIRST, PositionType.SECOND, PositionType.THIRD]
        i_pos = 0
        
        with self.mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
            while self.video.isOpened():
                ret, frame = self.video.read()
                if not ret:
                    continue
                    
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                image.flags.writeable = False

                results = pose.process(image)

                image.flags.writeable = True

                try:
                    landmarks = results.pose_landmarks.landmark

                    l_index = [landmarks[self.mp_pose.PoseLandmark.LEFT_INDEX.value].x,
                               landmarks[self.mp_pose.PoseLandmark.LEFT_INDEX.value].y]
                    r_index = [landmarks[self.mp_pose.PoseLandmark.RIGHT_INDEX.value].x,
                               landmarks[self.mp_pose.PoseLandmark.RIGHT_INDEX.value].y]

                    l_ear = [landmarks[self.mp_pose.PoseLandmark.LEFT_EAR.value].x,
                             landmarks[self.mp_pose.PoseLandmark.LEFT_EAR.value].y]           
                    r_ear = [landmarks[self.mp_pose.PoseLandmark.RIGHT_EAR.value].x,
                             landmarks[self.mp_pose.PoseLandmark.RIGHT_EAR.value].y]

                    l_wrist = [landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                               landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                    r_wrist = [landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                               landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

                    l_shoulder = [landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                               landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    r_shoulder = [landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                               landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]

                    l_hip = [landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].x,
                             landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    r_hip = [landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value].x,
                             landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value].y]

                    r_sw_dist = [dist(r_index, r_ear), dist(l_index, l_hip)]
                    l_sw_dist = [dist(l_index, l_ear), dist(r_index, r_hip)]

                    if r_sw_dist[0] < 0.1 and r_sw_dist[1] < 0.2:
                        sw_type = SwitchType.RIGHT
                        sec += 1
                    elif l_sw_dist[0] < 0.1 and l_sw_dist[1] < 0.2:
                        sw_type = SwitchType.LEFT
                        sec += 1
                    else:
                        sec = 0

                    if sec == 45:
                        sec = 0
                        self.counter = 0
                        i_pos = 0
                        if sw_type == SwitchType.RIGHT:
                            self.exercise_index += 1
                        elif sw_type == SwitchType.LEFT:
                            self.exercise_index -= 1

                        if np.abs(self.exercise_index) == len(self.exercise_list):
                             self.exercise_index = 0

                        self.changeExercise.emit(self.exercise_index)

                    if self.exercise_list[self.exercise_index] == ExerciseType.ARMS:
                        arms = Arms(l_shoulder, r_shoulder, l_wrist, r_wrist, l_hip, r_hip)
                        current_position = arms.position()

                        if current_position:
                            if not first_position:
                                first_position = current_position
                            else:
                                if current_position == first_position and last_position != first_position:
                                    self.counter += 1;
                                    self.changeCount.emit(self.counter)
                            last_position = current_position
                    elif self.exercise_list[self.exercise_index] == ExerciseType.LEFT_ARM:
                        l_arm = Arm(l_shoulder, l_wrist, l_hip)
                        if positions[i_pos] == l_arm.position():
                            i_pos += 1
                    elif self.exercise_list[self.exercise_index] == ExerciseType.RIGHT_ARM:
                        r_arm = Arm(r_shoulder, r_wrist, r_hip)
                        if positions[i_pos] == r_arm.position():
                            i_pos += 1

                    if i_pos == len(positions):
                        i_pos = 0
                        self.counter += 1
                        self.changeCount.emit(self.counter)

                    if self.detection_show:
                        self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS, 
                                                  self.mp_drawing.DrawingSpec(color=(14,66,160), thickness=2, circle_radius=2),
                                                  self.mp_drawing.DrawingSpec(color=(164,189,234), thickness=3, circle_radius=2))
                except:
                    pass

                q_image = qimage2ndarray.array2qimage(image)
                self.changePixmap.emit(q_image)
        
    @QtCore.Slot(int)
    def chooseExercise(self, exercise_index):
        self.exercise_index = exercise_index
        self.counter = 0
        
    @QtCore.Slot(int)
    def openVideo(self, camera_index):
        max_value_resolution = 10000
        self.video.open(camera_index, cv2.CAP_DSHOW)
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, max_value_resolution)
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, max_value_resolution)
        
    @QtCore.Slot()
    def closeVideo(self):
        self.video.release()
        cv2.destroyAllWindows()
        
    @QtCore.Slot()
    def manageDetection(self):
        if self.detection_show:
            self.detection_show = False
        else:
            self.detection_show = True


# In[ ]:


class MainWindow(QtWidgets.QMainWindow):
    changeExercise = QtCore.Signal(int)
    startDetection = QtCore.Signal(int)
    stopDetection = QtCore.Signal()
    
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.m_ui = Ui_MainWindow()
        self.m_ui.setupUi(self)
        
        self.setWindowIcon(QtGui.QIcon(":/ex_rep.ico"))
        
        self.exercise_list = [ExerciseType.ARMS, ExerciseType.LEFT_ARM, ExerciseType.RIGHT_ARM]
        self.exercise_index = 0
        self.m_ui.list_ex.setCurrentRow(self.exercise_index)
        self.m_ui.l_ex.setText(self.exercise_list[self.exercise_index].value)
        self.m_ui.list_ex.addItems([ex.value for ex in self.exercise_list])
        
        self.camera_active = False
        
        self.video_thread = VideoDetectionThread(self.exercise_list)
        self.video_resolution = []
        
        self.video_thread.changeCount.connect(self.setCount)
        self.video_thread.changeExercise.connect(self.chooseExercise)
        self.video_thread.changePixmap.connect(self.setImage)
        self.video_thread.finished.connect(self.m_ui.l_video.clear)
        
        self.changeExercise.connect(self.video_thread.chooseExercise)
        self.startDetection.connect(self.video_thread.openVideo)
        self.stopDetection.connect(self.video_thread.closeVideo)
        
        self.m_ui.list_ex.itemClicked.connect(self.chooseExerciseFromList)
        self.m_ui.pb_next_ex.clicked.connect(self.nextExercise)
        self.m_ui.pb_prev_ex.clicked.connect(self.prevExercise)
        self.m_ui.pb_camera.clicked.connect(self.manageVideo)
        self.m_ui.cb_detection.stateChanged.connect(self.video_thread.manageDetection)
        
    def closeEvent(self, event):
        if self.camera_active:
            QtWidgets.QMessageBox.warning(self,
                                          "Предупреждение",
                                          "Перед закрытием приложения остановите видео!")
            event.ignore()
        else:
            event.accept()
    
    @QtCore.Slot()
    def manageVideo(self):
        if not self.camera_active:
            try:
                camera_index = int(self.m_ui.le_cam.text())
                self.camera_active = True
                self.startDetection.emit(camera_index)
                self.video_thread.start()
                self.m_ui.pb_camera.setText("Выключить камеру")
            except:
                QtWidgets.QMessageBox.critical(self,
                                          "Ошибка",
                                          "В качестве номера камеры указано не числовое значение!")
        else:
            self.camera_active = False
            self.stopDetection.emit()
            self.video_resolution = []
            self.m_ui.pb_camera.setText("Включить камеру")
    
    def setExercise(self):
        row = self.exercise_index
        if row < 0 :
            row = len(self.exercise_list) + row
        self.m_ui.list_ex.setCurrentRow(row)
        
        self.m_ui.l_ex.setText(self.exercise_list[self.exercise_index].value) 
        self.m_ui.l_count.setText("0")
        
    @QtCore.Slot(int)
    def chooseExercise(self, exercise_index):
        self.exercise_index = exercise_index
        self.setExercise()
        
    @QtCore.Slot(QtWidgets.QListWidgetItem)
    def chooseExerciseFromList(self, item):
        self.exercise_index = self.m_ui.list_ex.row(item)
        self.setExercise()
        self.changeExercise.emit(self.exercise_index)
    
    @QtCore.Slot()
    def nextExercise(self):
        self.exercise_index += 1
        if self.exercise_index == len(self.exercise_list):
            self.exercise_index = 0
        self.setExercise()
        self.changeExercise.emit(self.exercise_index)
    
    @QtCore.Slot()
    def prevExercise(self):
        self.exercise_index -= 1
        if np.abs(self.exercise_index) == len(self.exercise_list):
            self.exercise_index = 0
        self.setExercise()
        self.changeExercise.emit(self.exercise_index)
    
    @QtCore.Slot(int)
    def setCount(self, count):
        self.m_ui.l_count.setText(str(count))
    
    @QtCore.Slot(QtGui.QImage)
    def setImage(self, image):
        pixmap = QtGui.QPixmap.fromImage(image)                     
        if not self.video_resolution:
            nod = math.gcd(pixmap.size().width(), pixmap.size().height())
            self.video_resolution = [pixmap.size().width() / nod, pixmap.size().height() / nod]
        self.m_ui.l_video.setPixmap(pixmap.scaled(
            self.m_ui.l_video.size().width(),
            self.m_ui.l_video.size().width() / self.video_resolution[0] * self.video_resolution[1]))


# In[ ]:


if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

