
import random
import csv
import time
import os 

PEDIDO =[]
nombre=[]
comuna_registrada=["San Bernardo","Calera de Tango","Buin"]
comuna=[]
pedido=[]
n_c=[]


def registrar_pedido():
   
    nombre=input("ingrese su nombre y apellido por favor :").lower()
    comuna=input("ingrese su comuna :\nSan Bernardo\nCalera de Tango\nBuin\n :").lower()
    if comuna is not comuna_registrada:
            print("Ingrese la comuna registrada en nuestro rango por favor")
    else:
            print(f"La comuna de{comuna} registrada con exito")    
    pedido=int( input("ingrese el detalle de su pedido :\n1. saco de 5kg\n2. saco de 10kg\n3. saco de 20kg\nseleccione una opcion : "))
    while True:
        if pedido==1:
            pedido="saco de 5kg"
            break
        elif pedido==2:
            pedido="saco de 10kg"
            break
        elif pedido==3:
            pedido="saco de 20kg " 
            break       
        else:
            print("seleccione una opcion valida")
            break

    PEDIDO.append[
            "Nombre":nombre,    
            "comuna":comuna,
            "pedido":pedido,
        ]
    
            
        


def listar_todos_los_pedidos():
  print("***Resumen de pedido")
  print("*"*50)
  print(f"Nombre :{nombre}")  
  print(f"comuna del pedido:{comuna}")
  print(f"su pedido es :{pedido}")

def imprimir_hoja_de_ruta():
    PEDIDO=["Nombre":nombre,    
            "comuna":comuna,
            "pedido":pedido,
            ]
    with open ("archivo.csv","w","") as csv_archivo:
        writer = csv.writer(csv_archivo)
        writer.writerow(PEDIDO)
