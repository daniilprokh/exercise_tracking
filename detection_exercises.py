#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from control_types import PositionType


# In[ ]:


import numpy as np


# In[ ]:


def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return angle 


# In[ ]:


def dist(a,b):
    a = np.array(a)
    b = np.array(b)

    d = np.sqrt(((a[0] - b[0])**2) + ((a[1] - b[1])**2))
    
    return d


# In[ ]:


class Arm():
    def __init__(self, shoulder, wrist, hip):
        self.angle = calculate_angle(wrist, shoulder, hip)

    def position(self):
        if self.angle < 30:
            return PositionType.FIRST
        elif self.angle > 80 and self.angle < 100:
            return PositionType.SECOND
        elif self.angle > 140:
            return PositionType.THIRD
        else:
            return None


# In[ ]:


class Arms():
    def __init__(self, l_shoulder, r_shoulder, l_wrist, r_wrist, l_hip, r_hip):
        self.l_d_angle = calculate_angle(l_wrist, l_shoulder, l_hip)
        self.l_u_angle = calculate_angle(l_wrist, l_shoulder, r_shoulder)
        self.r_d_angle = calculate_angle(r_wrist, r_shoulder, r_hip)
        self.r_u_angle = calculate_angle(r_wrist, r_shoulder, l_shoulder)
        self.l_dist = dist(l_wrist, l_hip)
        self.r_dist = dist(r_wrist, r_hip)
   
    def position(self):
        if self.r_d_angle > 160 and (self.r_u_angle > 80 and self.r_u_angle < 120) and (self.l_u_angle > 80 and self.l_u_angle < 120) and self.l_d_angle < 30:
            return PositionType.FIRST
        elif self.l_d_angle > 160 and (self.l_u_angle > 80 and self.l_u_angle < 120) and (self.r_u_angle > 80 and self.r_u_angle < 120) and self.r_d_angle < 30:
            return PositionType.SECOND
        else:
            return None

