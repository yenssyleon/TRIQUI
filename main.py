import random
import os
os.system("cls")
class Tablero():
    def __init__(self):
        self.celdas= [" "," "," "," "," "," "," "," "," "," "]  
        
    def salida(self):
        print(" %s | %s | %s " %(self.celdas[1], self.celdas[2], self.celdas[3]))
        print("-----------")
        print(" %s | %s | %s " %(self.celdas[4], self.celdas[5], self.celdas[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.celdas[7], self.celdas[8], self.celdas[9]))
        
    def update_celdas(self,ncelda,jugador):
        if self.celdas[ncelda]==" ":
            self.celdas[ncelda]=jugador
    
    def ganador(self, jugador):
        if self.celdas[1]== jugador and self.celdas[2]==jugador and self.celdas[3]==jugador:
            return True
        if self.celdas[4]== jugador and self.celdas[5]==jugador and self.celdas[6]==jugador:
            return True
        if self.celdas[7]== jugador and self.celdas[8]==jugador and self.celdas[9]==jugador:
            return True
        if self.celdas[1]== jugador and self.celdas[4]==jugador and self.celdas[7]==jugador:
            return True
        if self.celdas[2]== jugador and self.celdas[5]==jugador and self.celdas[8]==jugador:
            return True
        if self.celdas[3]== jugador and self.celdas[6]==jugador and self.celdas[9]==jugador:
            return True
        if self.celdas[1]== jugador and self.celdas[5]==jugador and self.celdas[9]==jugador:
            return True
        if self.celdas[3]== jugador and self.celdas[5]==jugador and self.celdas[7]==jugador:
            return True
        return False
    
    def empate(self):
        used_celdas=0
        for celdas in self.celdas:
            if celdas != " ":
                used_celdas +=1
            if used_celdas==9:
                return True
            else:
                return False
            
             
    
    def reset(self):
        
        self.celdas= [" "," "," "," "," "," "," "," "," "," "]  


        
Triqui=Tablero()


def print_encabezado():
    print ("Juguemos triqui.")
    
def refresh_screen():
    os.system("cls")

    print_encabezado()
    
    Triqui.salida()

while True:
    refresh_screen()
        
    x_choice = int(input("\nX, por favor elija la celda (1-9)"))

   #Actualizar triqui
    Triqui.update_celdas(x_choice,"X")
    
    refresh_screen()
    
    #Verificar si X es ganador 
    
    if Triqui.ganador("X"):
        print("\n X es el ganador\n")
        volver_a_jugar=input("¿Quiere volver a jugar? (SI/NO")
        if volver_a_jugar=="SI":
            continue
        else:
            break
        
    if Triqui.empate():
        print("\n Es un empate\n")
        volver_a_jugar=input("¿Quiere volver a jugar? (SI/NO")
        if volver_a_jugar=="SI":
            continue
        else:
            break
   
    o_choice = random.randint(1, 9)

   #Actualizar triqui
    Triqui.update_celdas(o_choice,"O")
    
    
    #Verificar si Y es ganador 
    
    if Triqui.ganador("O"):
        print("\n O es el ganador\n")
        volver_a_jugar=input("¿Quiere volver a jugar? (SI/NO")
        if volver_a_jugar=="SI":
            continue
        else:
            break