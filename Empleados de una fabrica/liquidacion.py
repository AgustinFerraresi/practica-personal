import os

empleados = [{'nombre':'Agustin Ferraresi','paga por hora':2500,'faltas':0},
             {'nombre':'Luca Cesano','paga por hora':2000,'faltas':0},
             {'nombre':'Juani Torti','paga por hora':1500,'faltas':0},
             {'nombre':'Marcelo Ferraresi','paga por hora':1700,'faltas':0},
             {'nombre':'Putun mi bebe','paga por hora':5000,'faltas':0},
             ]
#-------------------------------------------------------------------------------------------------
def buscar_empleado(x):
    
    indice=-1
    k=0
    for i in empleados:
        if x.lower() == empleados[k]['nombre'].lower():
            indice = k
            break
        else:
            k=k+1
    return indice
#-------------------------------------------------------------------------------------------------
#fun1 
def calcular_retenciones():
    k= 0 
    for i in empleados:
        salario_bruto = empleados[k]['paga por hora'] * 160
        
        if salario_bruto > 400000:
            aux = salario_bruto - 400000
            aux = aux * 0.35
            salario_bruto = salario_bruto - aux
        
        horas_faltadas = empleados[k]['faltas'] * 8
        retenciones = salario_bruto * 0.16
        valor_faltas = horas_faltadas * empleados[k]['paga por hora']
        
        salario_neto = salario_bruto - retenciones - valor_faltas
        
        print(f"El salario bruto del trabajador {k+1} es {salario_bruto} y el neto es {salario_neto}\n")    
        k= k+1   
        
    input("Presione ENTER para continuar")
    os.system('cls')
#-------------------------------------------------------------------------------------------------
#fun2
def nuevo_empleado():
    nombre = input("Ingrese el nombre y apellido del nuevo empleado ")
    
    #VALIDO QUE EL NOMBRE SOLO ESTE FORMADO POR LETRAS
    while nombre.isalpha():
        print("el nombre ingresado es invalido ")
        nombre = input("Ingrese nuevamente ")
    
    paga_x_hora = input("Ingrese la paga por hora del nuevo empleado ")
    
   # VALIDO QUE LO QUE SE INGRESE SEA UN VALOR NUMERICO ENTERO
    while not (paga_x_hora.isnumeric()):
        print("Ingresó un valor incorrecto ")
        paga_x_hora = input("Inténtelo nuevamente ")
     
    empleado_nuevo = {'nombre':nombre,'paga por hora':paga_x_hora,'faltas':0}
        
    empleados.append(empleado_nuevo)
    input("Presione ENTER para continuar")
#-------------------------------------------------------------------------------------------------
#fun3
def despedir_empleado():
    empleado_a_depedir=input("Ingrese el nombre y apellido del empleado a buscar ")
   
    while empleado_a_depedir.isalpha():
       print("ingresó un valor incorrecto")
       empleado_a_depedir=input("Ingrese nuevamente el nombre y apellido ")
   
    indice = buscar_empleado(empleado_a_depedir)
    
    if indice == -1:
       print("No se encontró el empleado")
    else:
       empleados.pop(indice)
       print("La lista de empleados se modificó exitosamente")
    
    input("Presione ENTER para continuar")
#-------------------------------------------------------------------------------------------------
#fun4 
def sumar_falta():
    sumar_falta = input("Ingrese el nombre y apellido del empleado al que le quiere sumar una falta \n")
    
    while sumar_falta.isalpha():
        print("ingresó un valor incorrecto")
        sumar_falta=input("Ingrese nuevamente el nombre y apellido ")
        
    indice = buscar_empleado(sumar_falta)
    
    if indice == -1:
        print("No se encontró el empleado")
    else:
        empleados[indice]['faltas'] = empleados[indice]['faltas'] +1
    print (empleados)
    
    input("Presione ENTER para continuar")
#-------------------------------------------------------------------------------------------------
#fun5
def mostrar_empleados():
    k=0
    for i in empleados:
        print(f"""
            Empleado: {empleados[k]['nombre']}
            Faltas: {empleados[k]['faltas']}
            --------------------------
              """)
        k=k+1
    
    input("Presione ENTER para continuar")
    os.system('cls')