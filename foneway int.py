# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:19:23 2023

@author: user
"""

import numpy as np
from scipy.stats import f_oneway
A1=np.array([12,13,15])
A2=np.array([15,21,25])
A3=np.array([54,89,86])
f_stat, p_value = f_oneway(A1,A2,A3)
if p_value < 0.05:
    print("Its a NULL Hypothesis")
else:
    print("Fail to reject NULL Hypothesis")
