#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:08:40 2018

@author: javierramirez
"""

import cv2
import numpy as np

main_dir = '/Users/javierramirez/Mineria de Datos/Datos/'
img_file=main_dir+'robot.png'
img=cv2.imread(img_file)
simply_means=cv2.mean(img)[:-1]
(means, stds)=cv2.meanStdDev(img)
stats=np.concatenate([means, stds]).flatten()