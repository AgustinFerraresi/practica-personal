import os
import liquidacion as liqui

rta=""

def menu():
    print("""
    ("1 - Cacular retenciones")
    ("2 - Agregar empleado")
    ("3 - Despedir empleado")
    ("4 - Sumar falta")
    ("5 - Mostrar salario bruto y neto")
    ("6 - Salir")
    """)

while rta != "salir":
    menu()
    op = input("Ingrese una opcion ")
    os.system('cls')
    if op.isnumeric():
        if int((op)) == 1:
           liqui.calcular_retenciones()
        elif int(op) == 2:
            liqui.nuevo_empleado()
        elif int(op) == 3:
            liqui.despedir_empleado()
        elif int(op) == 4:
            liqui.sumar_falta()
        elif int(op) == 5:
            liqui.mostrar_empleados()
            os.system('cls')
        elif int(op) == 6:
            rta = "salir"
        else:
            print("Ingresó una opcion no valida")
    else:
        ("Ingresó una opcion no NUMERICA")
        
    input("presione ENTER para continuar")
    os.system('cls')
print("Hasta la vista")