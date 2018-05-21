#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:06:20 2018

@author: javierramirez
"""

import cv2
import numpy as np

main_dir = '/Users/javierramirez/Mineria de Datos/Datos/'
img_file=main_dir+'robot.png'
img=cv2.imread(img_file)
rows, cols, dims=img.shape
means=np.zeros((dims))
std=np.zeros((dims))
for i in range(dims):
    mean=np.mean(img[:,:,i])
    std
    means[i]=mean