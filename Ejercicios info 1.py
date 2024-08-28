# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:09:52 2024

@author: yumop
"""
#ejercicio 1 
a=4
b=9
if a < b:
    print("el numero a es menor que el numero b")
elif a > b:
    print("el numero a es mayor que el numero b")
else:
    print("el numero a es igual que el numero b") 

#ejercicio 2
notas=[4.5,4.3,3.2,3.2,4.1]
porcentajes=[0.3,0.15,0.15,0.2,0.2]
ponderado=0
for i in range(0,4):
    ponderado=ponderado+notas[i]*porcentajes[i]
if ponderado > 3:
    print("Aprobado")
else:
    print("Reprobado")
print("el promedio del estudiante fue: "+ str(ponderado))

#Ejercicio 3
y=8
z=3
if y > z:
    x=1
    print("el valor de x es: "+ str(x))
elif y == z:
    x=2
    print("el valor de x es: "+ str(x))
else:
    x=3
    print("el valor de x es: "+ str(x))
    
#Ejercicio 4
cosas=[1,7,6]
cosas.sort(reverse=True)
print(cosas)

#Ejercicio 5
In=567890
nombres="camila fuentes saldarriaga"
patrimonio=19000000
estrato=4
porcentaje=0.03
matricula=50000
if patrimonio > 2000000 and estrato > 3 :
    matricula+= patrimonio*porcentaje
print(f"Numero de inscripción:{In} Nombre:{nombres} Valor de matricula:{int(matricula)}")

#Ejercicio 8
peso=[100,350,500]
tamano=[50,30,47]
densidad=[]
for i in range(0,2):
    densidad.append(peso[i]/tamano[i])
posicion=densidad.index(max(densidad))+1
print("la esfera mas densa es la numero ", posicion)

#Ejercicio 9
datos=[4,6,7,9]
mayor=max(datos)
menor=min(datos)
suma=mayor+menor
print("la suma del mayor y menor valor es: " + str(suma))    
    
#Ejercicios ciclos 1
a=4
b=6
M=0
i=1
while i <= b:
   M+=a
   i+=1
print("la multiplicacion es " + str(M))
    
#Ejercicio 2
notas=[5,3.5,4.2,0.5]
suma=0
i=0
while i < len(notas):
    suma+=notas[i]
    i+=1
promedio=suma/len(notas)
print("el promedio de la materia es " + str(promedio))

#Ejercicio 3
n=0
x=0
while n<=9:
    while x<=9:
        f= n**x
        print(f"el valor con n={n} y x={x} es {f}")
        x+=1
    n+=1
    x=0

#Ejercicio 4
n=7
suma=0
i=0
while i<=n:
    i+=1
    if i % 2!=0:
        suma+=i
print("la suma de numeros impares es " + str(suma))
        
#Ejercicio 5
n=4
fact=1
i=1
while i<n:
    i+=1
    fact=fact*i
    if i<n:
        continue
print("el factorial del numero es " + str(fact))

#Ejercicio 6
n=2
a=2
i=1
suma=0
while i<=2:
    suma+=(1/a)**i
    i+=1
print("la sumatoria es igual a " + str(suma))































    
    
    
    
    
    
    
    