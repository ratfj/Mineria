#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 11:29:27 2018

@author: javierramirez
"""

import cv2 as cv
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

main_dir = '/Users/javierramirez/Mineria de Datos/Datos/Perros/'

for i in range(1,21):
    img_file=main_dir+'fjrt_perro_'+str(i)+'.png'
    img=cv.imread(img_file)
    plt.figure(1)
    plt.imshow(img)
    plt.title("Robot")