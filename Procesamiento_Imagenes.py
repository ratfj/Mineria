#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:35:02 2018

@author: javierramirez
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

bgr_img=cv.imread('/Users/javierramirez/Mineria de Datos/Datos/robot.png')

###################Desplagar ventana con imagen, pero no funciona en Linux
#cv.imshow('Robot', bgr_img)
#cv.waitKey(0)
#cv.destroyAllWindows()
###################


plt.figure(1)
plt.imshow(bgr_img)
plt.title("Robot")

#Saving image to disk with OpenCV
cv.imwrite("/Users/javierramirez/Mineria de Datos/Datos/robot_opcv.png", bgr_img)

######Changin color spaces
#BGR -> Gray flag is cv.COLOR_BGR2GRAY
#BGR-> 
b,g,r=cv.split(bgr_img)
rgb_img=cv.merge([r,g,b])
gray_img=cv.cvtColor(bgr_img, cv.COLOR_BGR2GRAY)
hsv_img=cv.cvtColor(bgr_img, cv.COLOR_BGR2HSV)

#To Show image in the Console 
plt.figure()
plt.imshow(rgb_img)
plt.figure()
plt.imshow(gray_img)
plt.figure()
plt.imshow(hsv_img)

#Transformations cv.warp___

######Scaling
#fx and fy are resizing factors, 0.5 will result in half the size
half_img=cv.resize(rgb_img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
#(width, height)
fixed_img=cv.resize(rgb_img, (50,100), interpolation=cv.INTER_AREA)

plt.figure()
plt.imshow(half_img)
plt.figure()
plt.imshow(fixed_img)

######Rotation
#Splits the result from shape into three different values
rows, cols, dims=rgb_img.shape

M=cv.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rot_img=cv.warpAffine(rgb_img, M, (cols, rows))
plt.figure()
plt.imshow(rot_img)

####Mediana
mean_b= np.mean(b)
mean_g= np.mean(g)
mean_r=np.mean(r)

####Desviacion estandar
std_b= np.std(b)
std_g= np.std(g)
std_r=np.std(r)




