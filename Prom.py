#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:20:58 2018

@author: javierramirez
"""
##Valor mas grande de una lista
from numpy.random import randint as random

###########################

#rand_list= random(1,100,10) #Generar una lista aleatoria
##print(rand_list)
#
#aux=0
#
#for n in rand_list:
#    if n>aux:
#        aux=n
#
#print('El valor maximo de la lista', rand_list, 'es:', aux)
#        
 
      
############################ 

#s=[x**2 for x in range(10)]
#
#
#rand_list= random(10, size=10) #
#print(rand_list)
#
#
#M=[rand_list[x] for x in range(len(rand_list)) if x%2!=0 ]
#print(M)

#############################DICCIONARIOS

#rand_numbers=random(1,10,100)
#
#d={}
#
#for number in rand_numbers:
#    if number in d:
#        d[number]+=100
#    else:
#        d[number]=100
#
#print(d)
#print(d.values())
#print(d.keys())

###############################FUNCIONES

#def greet(name):
#    print("Hola", name)
#    return True
#
#greet('Alex')
#greet('Javier')
#greet('Miguel')

#n=input('Ingresa un numero:')
#
#digits=[]
#
#for element in n:
##    print(element)
#    digits.append(int(element))
#    
#print(digits)

################################ FIBONACCI
#def fibonacci(n):
#    a=0
#    b=1
#    while n>a:
#        print(a)
#        a, b = b, a+b
#    
#fibonacci(1000)

################################ CONCATENAR LISTAS
#lista1=['a','b','c']
#lista2=[1,2,3]
#lista3=[]
#
#def concatenar(lista1, lista2):
#    if len(lista1)==len(lista2):
#        for i in range(len(lista1)):
#            lista3.append(lista2[i])
#            lista3.append(lista1[i])
#    print(lista3)
#    
#    
#concatenar(lista1, lista2)


################################ PYTHON SETS
#
#basket={'apple', 'orange', 'banana', 'pear', 'orange'}
#
#basket2={'apple', 'orange', 'pineapple', 'strawberry'}
#
#print(basket-basket2)

################################ ZIP

#a=[1,2,3,4,5,6]
#b=['a', 'b', 'c', 'd','e', 'f']
#
#for x, y in zip(a,b): #Permite interar dos listas en un solo ciclo for
#    print(x, y)
    
    
################################ Asignar variables

#t=([1,2,3,4,5, 'x'],
#   [1,2,3,4,5,'y'],
#   [1,2,3,4,5,'z'])

#a,b,c=t


################################ FILE CONTROL



####### Escribir
#file= open('prueba.txt', 'w')
#
#file.write('Hola Mundo')
#
#file.close()

#with open('prueba.txt', 'w') as file:
#    file.write('Hello World')



####### Leer
#file= open('prueba.txt', 'r')
#
##print(file.read())
#
#for t in file.read():
#    print(t)
#    
#file.close()


#with open('prueba.txt', 'r') as file:
#    for line in file:
#        print(line)
    

#from itertools import count
#from itertools import permutations
#from itertools import combinations
#
#a=[1,2,3]
#
#for elem in combinations(a,2):
#    print(elem)
#    


a=[1,2,3,4,5,6]
b=['a', 'b', 'c', 'd','e', 'f']
c=zip(a,b)









