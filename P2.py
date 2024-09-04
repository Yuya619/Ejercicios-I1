# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:23:56 2024

@author: yumop
"""

gatos=[]
perros=[]
bienvenida="BIENVENIDOS A PATITAS CLINICA VETERINARIA"
print(bienvenida.center(90))
contp=1
contg=1
salir=False
while not salir:
    print("\n\n1.ingresar paciente\n2.cantidad de pacientes\n3.promedio de edad\n4.pacientes graves\n5.pacientes criticos\n6.buscar paciente por codigo de identificacion\n7.pacientes totales\n8.salir\n\n")
    seleccion=input("seleccione una opcion del menu: ")
    if int(seleccion)== 1:
        nombre=input("Nombre: ")
        tipo=input("Tipo de animal\n0 - si es gato\n1 - si es perro: ")
        edad=input("Edad: ")
        estado=input("Estado\n0 para grave\n1 para critico: ")
        if int(tipo)==0:
            cid="Felino"+f"{contg:03d}"
            gatos.append([nombre,tipo,edad,estado,cid])
            contg+=1
        elif int(tipo)==1:
            cid="Canino"+f"{contp:03d}"
            perros.append([nombre,tipo,edad,estado,cid])
            contp+=1
    elif int(seleccion)==2:
        patg=len(gatos)
        patp=len(perros)
        print(f"la cantidad de pacientes gatos es: {patg}\nla cantidad de pacientes perros es {patp} ")
    elif int(seleccion)==3:
        sg=0
        ng=0
        sp=0
        np=0
        for i in gatos:
            ng+=1
            edad=int(i[2])
            sg+=edad
        promeg=sg/ng
        print(f"El promedio de edad de los gatos es: {promeg} ")
        for i in perros:
            np+=1
            edad=int(i[2])
            sp+=edad
        promep=sp/np
        print(f"El promedio de edad de los perros es: {promep} ")
    elif int(seleccion)==4:
        pg=0
        for i in gatos:
            espa=i[3]
            if int(espa)==0:
                pg+=1
        print(f"Hay {pg} gatos en estado Grave")
        pp=0
        for i in perros:
            espa=i[3]
            if int(espa)==0:
                pp+=1
        print(f"Hay {pp} perros en estado Grave")
    elif int(seleccion)==5:
        pg=0
        for i in gatos:
            espa=i[3]
            if int(espa)==1:
                pg+=1
        print(f"Hay {pg} gatos en estado Critico")
        pp=0
        for i in perros:
            espa=i[3]
            if int(espa)==1:
                pp+=1
        print(f"Hay {pp} perros en estado Critico")
    elif int(seleccion)==6:
        idcode=input("ingrese codigo de id")
        for i in gatos:
            if idcode==i[4]:
                print(f"nombre: {i[0]}\ntipo: {i[1]}\nedad: {i[2]}\nestado: {i[3]}\ncodigo: {i[4]}")
        for i in perros:
            if idcode==i[4]:
                print(f"nombre: {i[0]}\ntipo: {i[1]}\nedad: {i[2]}\nestado: {i[3]}\ncodigo: {i[4]}")
    elif int(seleccion)==7:
        print(f"la cantidad total de pacientes es {len(perros)+len(gatos)}")
    elif int(seleccion)== 8: #Salir , deberá volver al menú inicial, igualmente si le da a la opción rechazar
       error=0 
       while error<3:
            print("\n\n1. Confirmar salida 🤙\n2. Rechazar salida❌")
            confirma=input("seleccione una opcion: ")
            if int(confirma)==1:
                salir=True
                break
            elif int(confirma)==2:
                break
            else:
                error+=1
    else:
        print("ingrese un valor valido")
            
            
            
            
            
            
