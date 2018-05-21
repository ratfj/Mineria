#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 16:16:09 2018

@author: javierramirez
EJERCICIOS
"""

"""
1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
"""

#def maximo(a, b):
#    if a>b:
#        return a
#    else:
#        return b
#    
#
#print(maximo(12,22))

"""
2- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. 
"""

#def valor_maximo (a,b,c):
#    if a>b and a>c:
#        return a
#    elif b>a and b>c:
#        return b
#    elif c>a and c>b:
#        return c
#    else:
#        print("Son iguales")
#    
#
#print(valor_maximo(123,145,188))
        
"""
3- Definir una función que calcule la longitud de una lista o una cadena dada. 
"""

#def longitud(lista):
#    suma=0
#    for i in lista:
#        suma+=1
#    return suma
#
#
#print(longitud("hola mundo"))

"""
4.- Escribir una función que tome un carácter y devuelva True si es una vocal, 
de lo contrario devuelve False.
"""

#def vocal(letra):
#    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
#        return True
#    else:
#        return False
#    
#
#print(vocal("o"))

"""
5.-Escribir una funcion sum() y una función multip() que sumen y multipliquen 
respectivamente todos los números de una lista.
"""
#def suma(lista):
#    suma=0
#    for i in lista:
#        suma+=i
#    print(suma)
#
#def mult(lista):
#    mult=1
#    for i in lista:
#        mult*=i
#    print(mult)  
#    
#    
#suma([1,2,3,4])
#mult([1,2,3,4])

"""
6.-Definir una función inversa() que calcule la inversión de una cadena.
"""

#def inversa(cadena):
#    cadena2=list(cadena)
#    cadena2.reverse()
#    cadn_inv=''.join(cadena2)
#    print(cadn_inv)
#
#
#inversa("hola mundo")

#def inversa(cadena):
#    cadena2=cadena[::-1]
#    print(cadena2)

#inversa("hola mundo")

"""
7.-Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

#def es_palindromo(word):
#    lis_word=list(word)
#    lis_word.reverse()
#    word_inv=''.join(lis_word)
#    if word_inv==word:
#        return True
#    else:
#        return False
#    
#
#print(es_palindromo("radar"))
    
"""
8.-Definir una función superposicion() que tome dos listas y 
devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
Escribir la función usando el bucle for anidado. 
"""

#def superposicion(lista1, lista2):
#    for i in lista1:
#        for y in lista2:
#            if i==y:
#                return True
#           
#    return False
#            
#    
#    
#print(superposicion([1,4,5], [2,6,1]))

"""
9.-Definir una función generar_n_caracteres() que tome un entero n 
y devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

#def generar_n_caracteres(n, caracter):
#   print(n*caracter)
#       
#generar_n_caracteres(5, "o")
#    

"""
10.-Definir un histograma procedimiento() que tome una lista de números enteros 
e imprima un histograma en la pantalla. 
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
"""
#def asteriscos(lista):
#    for n in lista:
#        print(n*"*")
#
#
#asteriscos([1,3,1])
    
"""

P A R T E    2

"""

"""
1.-Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
"""

#def max_in_list(lista):
#    aux=-100
#    for i in lista:
#        if i>aux:
#            aux=i
#    return aux
#
#print(max_in_list([-2,8,9,112,44]))
 
"""
2.-Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga
"""

#def mas_larga(lista):
#    aux="x"
#    for word in lista:
#        if len(word)>len(aux):
#            aux=word
#    return aux
#
#print(mas_larga(["hola", "Nathaly", "papa", "queso"]))
        
"""
3.-Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, 
y devuelva las palabras que tengan mas de n caracteres.
"""

#def filtrar_palabras(lista, n):
#    lista2=[]
#    for word in lista:
#        if len(word)>n:
#            lista2.append(word)
#    print(lista2)
#
#
#filtrar_palabras(["hola", "mama", "Nathaly", "Javier", "Jose"], 4)
            
"""
4.-Escribir un programa que le diga al usuario que ingrese una cadena. 
El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene. 
"""
#cadena=input('Ingrsa una cadena: ')
#count=0
#for l in cadena:
#    if l.isupper():
#        count+=1
#print(count)
    
"""
5.-Construir un pequeño programa que convierta números binarios en enteros. 
"""

"""
6.-Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""

#año_actual=int(input("Ingrsa el año actual: "))
#name1= input("Ingresa el nombre de la persona1: ")
#born1= int(input("Ingrsa año de nacimiento: "))
#name2= input("Ingresa el nombre de la persona2: ")
#born2= int(input("Ingrsa año de nacimiento: "))
#name3= input("Ingresa el nombre de la persona3: ")
#born3= int(input("Ingrsa año de nacimiento: "))
#
#print(name1, 'Cumplira:', año_actual-born1, 'años')
#print(name2, 'Cumplira:', año_actual-born2, 'años')
#print(name3, 'Cumplira:', año_actual-born3, 'años')

"""
7.-Definir una tupla con 10 edades de personas. 
Imprimir la cantidad de personas con edades superiores a 20.
"""

#lista_edades=[]
#
#edad=int(input("Ingresa una edad: "))
#lista_edades.append(edad)
#opc=int(input("¿Otra edad? Si=1, No=0 :"))
#
#while opc==1:
#    edad=int(input("Ingresa una edad: "))
#    lista_edades.append(edad)
#    opc=int(input("¿Otra edad? Si=1, No=0 :"))
#
#edades=tuple(lista_edades)
#count=0
#for p in edades:
#    if p>20:
#        count+=1
#print('Existen', count, 'personas con edades superiores a 20.')

"""
8.-Definir una lista con un conjunto de nombres, 
imprimir la cantidad de nombres que comienzan con la letra a.
"""
#names=[]
#count=0
#
#print('Ingresa x para dejar de ingresar nombres')
#name="z"
#
#
#while name!="x":
#    name=input('Nombre: ')
#    names.append(name)
#
#letra=input('Nombres que comienzan con la letra:')
#
#list_names=[]
#for name in names:
#    if name[0]==letra.upper() or name[0]==letra.lower():
#        list_names.append(name)
#        count+=1
#
#print('La cantidad de nombres que comienzan con la letra',letra.upper(),'o', letra.lower(), 'es', count)
#print('Y son:', list_names)

"""
9.-Crear una función contar_vocales(), 
que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene 
y así hasta completar todas las vocales.
"""

#def contar_vocales(word):
#    count_a=0
#    count_e=0
#    count_i=0
#    count_o=0
#    count_u=0
#    
#    for w in word:
#        if w=="a" or w=="A":
#            count_a+=1
#        elif w=="e" or w=="E":
#            count_e+=1
#        elif w=="i" or w=="I":
#            count_i+=1
#        elif w=="o"or w=="O":
#            count_o+=1
#        elif w=="u"or w=="U":
#            count_u+=1
#     
#     
#            
#    print("La palabra:", word, "tiene a:",count_a,"e:", count_e, 'i:', count_i, 'o:',count_o, 'u:', count_u)
#    
#    
#word=input("Ingresa una palabra:")
#contar_vocales(word)

"""
10.-Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.
Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
"""

#def bisiesto(year):
#
#    if year%4==0 or year%400==0:
#        if year%100==0:
#            print("No es bisiesto")
#        else:
#            print("Es bisiesto")
#    else:
#        print("No es bisiesto")
#
#year=int(input("Ingresa un año: "))
#bisiesto(year)

#if __name__ == '__main__':
#    n = int(input())
#    arr = map(int, input().split())
#    lista=list(arr)
#    lista.sort(reverse=True)
#    maximo=lista[0]
#    second=0
#    for i in range(len(lista)):
#        if lista[i]<maximo:
#            second=lista[i]
#            print(second)
#            break
#   
     
"""
E  X  T  R  A  S
http://www.lsi.us.es/docencia/get.php?id=9066
"""

"""
a)Inserte el caracter entre cada letra de la cadena. Ej: ’separar’ y ’,’ debería devolver
’s,e,p,a,r,a,r’
"""

#def separar(cadena):
#    
#    coma=","
#    new_cadena=""
#    len_cadena=len(cadena)
#    i=1
#
#    for w in cadena:
#        if i==len_cadena:
#            new_cadena+=w
#            
#        else:
#            new_cadena+=w+coma
#            i+=1
#    print(new_cadena)
#
#
#separar("separar")

"""
b) Reemplace todos los espacios por el caracter. Ej: ’mi archivo de texto.txt’ y ’_’
debería devolver ’mi_archivo_de_texto.txt’ 
"""

#def remplazar(cadena):
#
#    new_cadena=""
#    
#    for palabra in cadena:
#        if palabra==" ":
#            new_cadena+="_"
#        else:
#            new_cadena+=palabra
#        
#    print(new_cadena)
#   
#remplazar("mi archivo de texto.txt")     
   
"""
c) Reemplace todos los dígitos en la cadena por el caracter. Ej: ’su clave es: 1540’ y
’X’ debería devolver ’su clave es: XXXX’ 
"""

#def remplazar(cadena):
#    new_cadena=""
#    
#    for i in cadena:
#        new_cadena+="X"
#        
#    print(new_cadena)
#
#
#remplazar("1540")    

"""
d) Inserte el caracter cada 3 dígitos en la cadena. Ej. ’2552552550’ y ’.’ debería
devolver ’255.255.255.0’ 
""" 

#def insertar(cadena):
#    new_cadena=""
#    count=1
#    
#    for n in cadena:
#        if count%3==0:
#            new_cadena+=n+"."
#            count+=1
#        else:
#            new_cadena+=n
#            count+=1
#            
#    print(new_cadena)
#
#insertar("2552552550")

#list_cadena.insert(count, ".") #para insertar un valor en una lista: (posicion, valor)
   

"""
e) Crear una funcion con dos cadenas que indique si la segunda cadena es una subcadena de la primera. 
Por ejemplo, ’cadena’ es una subcadena de ’subcadena’. 
"""
#
#def is_subcadena(cadena1, cadena2):
#    
#    if cadena2 in cadena1:
#        print(True)
#    else:
#        print(False)
#
#is_subcadena("subcadena", "cadena")

"""
f)Crear una funcion con dos cadenas que devuelva la que sea anterior en orden alfábetico. 
 Por ejemplo, si recibe ’kde’ y ’gnome’ debe devolver ’gnome’.
"""

#def orden(cadena1, cadena2):
#    space=" "
#    print(sorted((cadena1+space+cadena2).split()))
#
#orden("kde", "gnome")

#def orden(cadena1, cadena2):
#    list_cadenas=[]
#    list_cadenas.append(cadena1)
#    list_cadenas.append(cadena2)
#    list_cadenas.sort()
#    print(list_cadenas[0])
#    
#    
#
#orden("kde", "gnome")

"""
T U P L A S / L I S T A S
"""

"""
a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima 
   el mensaje: Estimado <nombre>, vote por mí. 
"""

#def saludo(tupla):
#    for name in tupla:
#        print('Estimado',name+",",'vote por mí.')
#
##nombres=("Francisco", "Alejandro", "Jaime")
##saludo(nombres)
#
##Dando el usuario los nombres:

#n=int(input()) #Numero de bombres
#arr = map(str, input().split()) #Insertar nombres separados por un espacio
#tupla=tuple(arr) #Convetir en tupla
#saludo(tupla) #Llamar la funcion 

"""
b) Escribir una función que reciba una tupla con nombres, una posición de origen py
una cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a
partir de la posición p. 
"""

#def saludo(tupla, py, n):
#    p=py-1 #Para que cuente la posicion partiendo de 1
#    for i in range(n):
#        if n<len(tupla):
#            print('Estimado',tupla[p+i]+',','vote por mí')
#        else:
#            print('No hay suficientes nombres para mostrar partiendo de la posicion indicada')
#            break
#            
#        
#
#tupla=("Pedro", "Juan", "Pepe", "Raul")
#saludo(tupla, 2, 2)

"""
c) Escribir una función que reciba nombre y genero y que para cada nombre imprima el mensaje: 
    Estimado <nombre>, vote por mí. 
 Teniendo en cuenta el género del destinatario, para ello, deberá recibir una tupla de tuplas, 
 conteniendo el nombre y el género.
"""

#def saludo(tupla, g):
#   
#    for elemento in tupla:
#        for genero in elemento:
#            if genero==g and g=="F":
#                 print('Estimada', elemento[0]+",",'vote por mí.')
#            elif genero==g and g=="M":
#                print('Estimado', elemento[0]+",",'vote por mí.')
#            
#        
#
#tupla=(("Juan", "M"), ("Pepe", "M"), ("Nathaly", "F"), ("Alejandra", "F"), ("Jaime", "M"))
#saludo(tupla, "M")

"""
d)  Escribir una función que reciba una tupla de tuplas con nombres y genero, una posición de origen py,
una cantidad n, e imprima el mensaje anterior para los n nombres del genero indicado que se encuentran a
partir de la posición p. 
"""

#def saludo(tupla, g, py, n):
#    py=py-1
#    for i in range(n):
#        if g in tupla[py+i]:
#            for elemento in tupla[py+i]:
#                if g=="F":
#                    print('Estimada', elemento +",",'vote por mí.')
#                    break
#                else:
#                    print('Estimado', elemento +",",'vote por mí.')
#                    break
#        
#            
#tupla=(("Juan", "M"), ("Pepe", "M"), ("Nathaly", "F"), ("Alejandra", "F"), ("Jaime", "M"))
#saludo(tupla, "F", 2, 4)

"""
d)Escribir una función que reciba una lista de tuplas (Apellido, Nombre,
Inicial_segundo_nombre) y devuelva una lista de cadenas donde cada una contenga
primero el nombre, luego la inicial con un punto, y luego el apellido. 
"""

#def unir_nombres(tupla):
#    cadena=""
#    list_name=[]
#    for elemento in tupla:
#        cadena=elemento[1]+" "+elemento[2]+"."+" "+elemento[0]
#        list_name.append(cadena)
#    print(list_name)
#    
#tupla=(("Ramirez", "Francisco", "J"),("Gomez", "Nathaly", "J"), ("Gonzales", "Luis", "A"))
#unir_nombres(tupla)    


"""
Ejercicio 1. Agenda simplificada
Escribir una función que reciba una cadena a buscar y una lista de tuplas
(nombre_completo, telefono), y busque dentro de la lista, todas las entradas que
contengan en el nombre completo la cadena recibida (puede ser el nombre, el apellido
o sólo una parte de cualquiera de ellos). Debe devolver una lista con todas las tuplas
encontradas. 
"""


#def directorio(buscar, lista):
#    
#    result_list=[]
#    for tupla in lista:
#        if len(buscar)<2:
#            if buscar.lower() in tupla[0] or buscar.upper() in tupla[0]:
#                result_list.append(tupla)
#        else:
#            if buscar.lower() in tupla[0] or buscar in tupla[0]:
#                result_list.append(tupla)
#    
#    print(result_list)
#       
#        
#lista=[("Javier Ramirez Trejo", 4611837264), 
#       ("Nathaly Gomez Millán", 4131157466),
#       ("Jaime Perez", 4611234567),
#       ("Adalberto Perez", 7861234567)]
#        
#buscar=input("Ingresa un nombre o inicial para buscar: ")
#
#directorio(buscar, lista)
#directorio("Ram", lista)
    
"""
D I C C I O N A R I O

Insertar datos: diccionario[clave] = valor
"""

       
"""
Ejercicio 1. Continuación de la agenda.
Escribir un programa que vaya solicitando al usuario que ingrese nombres.
a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe
mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. 
b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
El usuario puede utilizar la cadena "*", para salir del programa. 
"""

directorio={"Javier Ramirez Trejo": 4611837264,
            "Nathaly Gomez Millán": 4131157466,
            "Jaime Perez": 4611234567,
            "Adalberto Perez":7861234567}


opc="z"
print("Usa '*' para salir")
print("1: Sí, 0: No")

while opc=="z":
    name=input("Ingresa un nombre: ")
    if name=="*":
        opc="*"
    elif name in directorio:
        print('Numero: ', directorio[name])
        edit=int(input('¿Desea editar numero?: '))
        if edit==1:
            upd_number=int(input('Nuevo numero: '))
            directorio[name]=upd_number
            print('[Numero actualizado]')
        
    else:
        add=int(input(name+" no existe en el directorio, ¿Desea agregar?: "))
        if add==1:
            number=int(input('Ingresa un numero para '+name+': '))
            directorio[name]=number
            print('[Agregado Correctamente]')
        
        
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    