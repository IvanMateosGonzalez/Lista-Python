from comun import Comun
from funciones import Funciones

lista = ["a", "b", "c", "d", "e", "f"]

com = Comun

fun = Funciones

run = 1

while run == 1:
    menu = {"0":"0)Terminar"}

    menu["1"] = "1)Crear lista" 

    if 'lista' in globals():
        menu["2"] = "2)Añadir elemento"
        if len(lista) > 0:
            menu["3"] = "3)Eliminar elemento"
            menu["4"] = "4)Modificar elemento"
            menu["5"] = "5)Mostrar datos"
            menu["6"] = "6)Mostrar datos de manera invrersa"
            menu["7"] = "7)Limpiar lista"
            menu["8"] = "8)Borrar lista"
    
    for opc in menu:
        print(menu[opc])
    seleccion = str(input("\n :"))
    com.limpiar()
    if seleccion in menu:
        selec_int = int(seleccion)
        if selec_int == 0:
            run = 0
        elif selec_int == 1:
            lista = []
        elif selec_int == 2:
            fun.dos(lista)
            com.limpiar()
        elif selec_int == 3:
            fun.tres(lista)
            com.limpiar()
            print("Elemento eliminado")
        elif selec_int == 5:
            fun.cinco(lista)
            com.limpiarEspera()
        elif selec_int == 6:
            fun.seis(lista)
            com.limpiarEspera()
        elif selec_int == 7:
            lista.clear()
            com.limpiar()
            print("Lista limpiada")
        elif selec_int == 8:
            del lista
            com.limpiar()
            print("Lista borrada")
    else:
        print("Elige una opcion valida")
    
    del menu
    
        

        
    