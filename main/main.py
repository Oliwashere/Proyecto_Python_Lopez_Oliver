from funciones.funciones import *
from menus.menus import *

while True:
    clear_screen()
    opct=0
    opcS=0
    opc = menu_principal()
    clear_screen()

    if opc == 1:
        while True:
            clear_screen()
            opcC = menu_cord()
            if opcC == 1:
                menu_reg_camp("campers.json")
                if opcS == 1:
                    break  
            elif opcC == 2:
                menu_mostrar_camp("campers.json")
                if opcS == 1:
                    break  
            elif opcC == 3:
                menu_editar_camp("campers.json")
                if opcS == 1:
                    break      
            elif opcC == 4:
                menu_eliminar_camp("campers.json")
                if opcS == 1:
                    break  
            elif opcC == 5:
                menu_reg_notas("campers.json")
                if opcS == 1:
                    break 
            elif opcC == 6:
                menu_gestion_rutas(rutas_entrenamiento, "trainers.json")    
            elif opcC == 7:
                menu_mostrar_trainers("trainers.json")
                if opcS == 1:
                    break     
            elif opcC == 9:
                break  
    elif opc == 2:
        opct=menu_train("trainers.json")
        if opct==1:
            menu_mostrar_trainers("trainers.json")
            if opcS == 1:
                break  
    elif opc == 3:
        menu_salir()
        break  



