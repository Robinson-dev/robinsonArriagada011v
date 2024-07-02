"""
robinsonArriagada_011v
"""
import funciones  as fn
import random
import csv
import time
import os 

clear="cls"



while True:
    try:
        print("""
            ***BIENVENIDOS A CATPREMIUM***
            
            1. Registar Pedido
            2. Listar todos los Pedidos
            3. Imprimir hoja de Ruta
            4. Salir del programa
                                """)
        opcion = int(input("        ingrese una opcion :"))
        if opcion==1:
                fn.registrar_pedido()
        elif opcion==2:
                fn.listar_todos_los_pedidos()
        elif opcion==3:
                fn.imprimir_hoja_de_ruta()
        elif opcion==4:
                print("Saliendo del programa...")
                break 
                
        else :
                print("ingrese una opcion valida")
                time.sleep(1)

    except ValueError:
           print("ERROR, ingrese una opcion valida ")
           time.sleep(2)
        

           print("""
            ***BIENVENIDOS A CATPREMIUM***
            
            1. Registar Pedido
            2. Listar todos los Pedidos
            3. Imprimir hoja de Ruta
            4. Salir del programa
                                """)
    opcion = int(input("        ingrese una opcion :"))








































