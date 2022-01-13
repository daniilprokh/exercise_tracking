#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from enum import Enum


# In[ ]:


class ExerciseType(Enum):
    ARMS = "Поочерёдное поднятие рук вверх"
    LEFT_ARM = "Круговые движения левой рукой"
    RIGHT_ARM = "Круговые движения правой рукой"


# In[ ]:


class PositionType(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3


# In[ ]:


class SwitchType(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2

