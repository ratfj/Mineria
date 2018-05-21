#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:22:02 2018

@author: javierramirez
"""
import numpy as np
import re

a=list(range(70)) #0-69
b=list(range(70,140)) #70-139
c=list(range(140, 210)) #140-209


main_dir = '/Users/javierramirez/Mineria de Datos/Datos/'
n_friend='1'
file='fb_posts_'+n_friend+'.txt'

with open(main_dir+file, 'r', encoding='utf-8') as content_file:
        text= content_file.read()

text=text.lower()
words=re.findall('[a-záéíóúñ]+', text)
Eliminado= set(words)
Eliminado=list(Eliminado)

with open(main_dir+file, 'r') as inp:
    lines=[]
    for line in inp:
        lines.append(line.lower())
    


lectura = open("train_data.txt",'r')
lineas = lectura.readlines()
escritura = open("train_data.txt","w")
for linea in lineas:
	escritura.write(lines)







WordVector=[]

for eachline in lines:
    Vector = []
    for Counts in Eliminado:
        Vector.append(eachline.count(Counts))
    WordVector.append(Vector)
    
#lgt = len(Vector)
#df = np.zeros(lgt, int)
#aux = 0
#
#for row in WordVector:
#    for column in row:
#        if column > 0:
#            df[aux] += 1 
#        aux += 1
#    aux = 0
    

