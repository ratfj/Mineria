#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:17:41 2018

@author: javierramirez
"""

import cv2 as cv
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

main_dir = '/Users/javierramirez/Mineria de Datos/Datos/'
img_file=main_dir+'robot.png'
img=cv.imread(img_file)


hist_1=cv.calcHist([img], [2], None, [32], [0, 256])
plt.plot(hist_1, color = 'r')

hist_2=cv.calcHist([img], [1,0], None, [32,32], [0,256,0, 256])
plt.figure()
plt.imshow(hist_2)
plt.title("2D color histogram for green and blue")

hist_3=cv.calcHist([img], [0,1,2], None, [32,32,32], [0,256,0,256])
hist_f=hist_3.flatten()

hist_f_norm=normalize(hist_f)