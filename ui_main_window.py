# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1305, 693)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(164, 189, 234, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(209, 222, 244, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(82, 94, 117, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(109, 126, 156, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.t_ex = QLabel(self.centralwidget)
        self.t_ex.setObjectName(u"t_ex")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.t_ex.sizePolicy().hasHeightForWidth())
        self.t_ex.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Palatino Linotype")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.t_ex.setFont(font)

        self.verticalLayout_2.addWidget(self.t_ex)

        self.list_ex = QListWidget(self.centralwidget)
        self.list_ex.setObjectName(u"list_ex")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.list_ex.sizePolicy().hasHeightForWidth())
        self.list_ex.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"Palatino Linotype")
        font1.setPointSize(16)
        self.list_ex.setFont(font1)
        self.list_ex.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.list_ex)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_next_ex = QPushButton(self.centralwidget)
        self.pb_next_ex.setObjectName(u"pb_next_ex")
        sizePolicy1.setHeightForWidth(self.pb_next_ex.sizePolicy().hasHeightForWidth())
        self.pb_next_ex.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(8)
        self.pb_next_ex.setFont(font2)
        self.pb_next_ex.setContextMenuPolicy(Qt.NoContextMenu)
        self.pb_next_ex.setStyleSheet(u"background-color: rgb(14, 66, 160);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pb_next_ex)

        self.pb_prev_ex = QPushButton(self.centralwidget)
        self.pb_prev_ex.setObjectName(u"pb_prev_ex")
        sizePolicy1.setHeightForWidth(self.pb_prev_ex.sizePolicy().hasHeightForWidth())
        self.pb_prev_ex.setSizePolicy(sizePolicy1)
        self.pb_prev_ex.setStyleSheet(u"background-color: rgb(14, 66, 160);\n"
"color: rgb(255, 255, 255);")
        self.pb_prev_ex.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pb_prev_ex)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.t_progress = QLabel(self.centralwidget)
        self.t_progress.setObjectName(u"t_progress")
        sizePolicy.setHeightForWidth(self.t_progress.sizePolicy().hasHeightForWidth())
        self.t_progress.setSizePolicy(sizePolicy)
        self.t_progress.setFont(font)

        self.verticalLayout_2.addWidget(self.t_progress)

        self.t_current_ex = QLabel(self.centralwidget)
        self.t_current_ex.setObjectName(u"t_current_ex")
        sizePolicy.setHeightForWidth(self.t_current_ex.sizePolicy().hasHeightForWidth())
        self.t_current_ex.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"Palatino Linotype")
        font3.setPointSize(18)
        self.t_current_ex.setFont(font3)

        self.verticalLayout_2.addWidget(self.t_current_ex)

        self.l_ex = QLabel(self.centralwidget)
        self.l_ex.setObjectName(u"l_ex")
        sizePolicy1.setHeightForWidth(self.l_ex.sizePolicy().hasHeightForWidth())
        self.l_ex.setSizePolicy(sizePolicy1)
        self.l_ex.setMinimumSize(QSize(600, 0))
        font4 = QFont()
        font4.setFamily(u"Palatino Linotype")
        font4.setPointSize(22)
        self.l_ex.setFont(font4)
        self.l_ex.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.l_ex.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.l_ex)

        self.t_count = QLabel(self.centralwidget)
        self.t_count.setObjectName(u"t_count")
        sizePolicy.setHeightForWidth(self.t_count.sizePolicy().hasHeightForWidth())
        self.t_count.setSizePolicy(sizePolicy)
        self.t_count.setFont(font3)

        self.verticalLayout_2.addWidget(self.t_count)

        self.l_count = QLabel(self.centralwidget)
        self.l_count.setObjectName(u"l_count")
        sizePolicy1.setHeightForWidth(self.l_count.sizePolicy().hasHeightForWidth())
        self.l_count.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamily(u"Palatino Linotype")
        font5.setPointSize(30)
        self.l_count.setFont(font5)
        self.l_count.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.l_count.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.l_count)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.l_video = QLabel(self.centralwidget)
        self.l_video.setObjectName(u"l_video")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.l_video.sizePolicy().hasHeightForWidth())
        self.l_video.setSizePolicy(sizePolicy2)
        self.l_video.setMinimumSize(QSize(600, 480))
        self.l_video.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.l_video.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.l_video)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.t_cam = QLabel(self.centralwidget)
        self.t_cam.setObjectName(u"t_cam")
        sizePolicy.setHeightForWidth(self.t_cam.sizePolicy().hasHeightForWidth())
        self.t_cam.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamily(u"Palatino Linotype")
        font6.setPointSize(14)
        self.t_cam.setFont(font6)

        self.horizontalLayout_2.addWidget(self.t_cam)

        self.le_cam = QLineEdit(self.centralwidget)
        self.le_cam.setObjectName(u"le_cam")
        sizePolicy1.setHeightForWidth(self.le_cam.sizePolicy().hasHeightForWidth())
        self.le_cam.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setFamily(u"Palatino Linotype")
        font7.setPointSize(12)
        self.le_cam.setFont(font7)
        self.le_cam.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.le_cam.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.le_cam)

        self.cb_detection = QCheckBox(self.centralwidget)
        self.cb_detection.setObjectName(u"cb_detection")
        sizePolicy.setHeightForWidth(self.cb_detection.sizePolicy().hasHeightForWidth())
        self.cb_detection.setSizePolicy(sizePolicy)
        self.cb_detection.setFont(font6)
        self.cb_detection.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_2.addWidget(self.cb_detection, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pb_camera = QPushButton(self.centralwidget)
        self.pb_camera.setObjectName(u"pb_camera")
        sizePolicy1.setHeightForWidth(self.pb_camera.sizePolicy().hasHeightForWidth())
        self.pb_camera.setSizePolicy(sizePolicy1)
        self.pb_camera.setFont(font1)
        self.pb_camera.setStyleSheet(u"background-color: rgb(14, 66, 160);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.pb_camera)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1305, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0435\u043a\u0438\u043d\u0433 \u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u0439", None))
        self.t_ex.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u044f", None))
        self.pb_next_ex.setText(QCoreApplication.translate("MainWindow", u"\u25bc", None))
        self.pb_prev_ex.setText(QCoreApplication.translate("MainWindow", u"\u25b2", None))
        self.t_progress.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441", None))
        self.t_current_ex.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0435\u0435 \u0443\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u0435", None))
        self.l_ex.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u044f", None))
        self.t_count.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0434\u0445\u043e\u0434\u043e\u0432", None))
        self.l_count.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_video.setText("")
        self.t_cam.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u043c\u0435\u0440\u044b", None))
        self.le_cam.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cb_detection.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0434\u0435\u0442\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.pb_camera.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043a\u0430\u043c\u0435\u0440\u0443", None))
    # retranslateUi

