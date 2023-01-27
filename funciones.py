import os
from comun import Comun

com = Comun

class Funciones:
    def dos(lista):
        print("Escribe 'exit() para salir\n")
        run = 1
        num = len(lista)
        while run == 1:
            val = str(input(f"{num}: "))
            if val == "exit()":
                run = 0
            elif val != "":
                num = num + 1
                lista.append(val)
    def tres(lista):
        i = 0
        run = 1
        for x in lista:
            print(f"{i}) {x}")
            i = i+1
        while run == 1:
            opc = int(input("Seleccione el objeto a eliminar: "))
            if opc < len(lista) and opc >= 0:
                del lista[opc]
                run = 0
            else:
                print("Ese elemento no existe")
    def cinco(lista):
        i = 0
        for x in lista:
            print(f"{i}) {x}")
            i = i+1
    def seis(lista):
        reverso = lista.copy()
        reverso.reverse()
        i = len(lista) - 1
        for x in reverso:
            print(f"{i}) {x}")
            i = i-1