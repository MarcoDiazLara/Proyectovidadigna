import random
import matematicas as mat
from tkinter import *
from tkinter import ttk


def suma():
    llave_suma = True
    entrada = True
    contador = 0
    cota_sup = num_A
    while(entrada):
        llave_suma = True
        while(llave_suma):
            A = random.randint(0,cota_sup)
            B = random.randint(0,cota_sup)
        
            if((A+B)<cota_sup):
                llave_suma = False
            
        print(A,"+",B,"=")
        res = int(input())
    
        if(res == (A+B)):
            contador += 1
            print("Felicidades, Acertaste!!!!")
            if(contador == 1):
                print("Haz, acertado: ",contador,"suma")
            else:
                print("Haz, acertado: ",contador,"sumas")
            
        else:
            print("Muy mal, esa no es la respuesta")
            entrada = False
        
def resta():
    llave_resta = True
    entrada = True
    contador = 0
    cota_sup = num_A
    while(entrada):
        llave_resta = True
        while(llave_resta):
            A = random.randint(0,cota_sup)
            B = random.randint(0,cota_sup)
            
            if(((A-B)<cota_sup) & ((A-B)>=0)):
                llave_resta = False
        print(A,"-",B,"=")
        res = int(input())
        
        if(res == A-B):
            contador += 1
            print("Felicidades, Acertaste!!!!")
            if(contador == 1):
                print("Haz acertado: ",contador,"resta")
            else:
                print("Haz acertado: ",contador,"restas")
        else:
            print("Muy mal, esa no es la respuesta")
            entrada = False

def multi():
    entrada = True
    llave_multi = True
    contador = 0
    cota_sup = num_A
    while(entrada):
        llave_multi = True
        while(llave_multi):
            A = random.randint(1,cota_sup)
            B = random.randint(1,cota_sup)
            
            if((A*B)<=cota_sup):
                llave_multi = False
        print(A,"*",B,"=")
        res = int(input())
        
        if(res == A*B):
            contador += 1
            print("Felicidades, Acertaste!!!!")
            if(contador == 1):
                print("Haz acertado: ",contador,"multiplicacion")
            else:
                print("Haz acertado: ",contador,"multiplicaciones")
        else:
            print("Muy mal, esa no es la respuesta")
            entrada = False

    

def Salir():
    root.destroy()
    
 
#Iniciacion de la interfaz grafica
root = Tk()
root.geometry("1000x600")
root.title("Practica Profesional")
root["bg"] = "#26867d"
root.resizable(False,False)

#Colocacion del logo
imagen = PhotoImage(file = "Imagenes/Logo.png")
fondo = Label(root, image = imagen, bg = "#26867d" ).place(x = 400, y = 200)


#Creacion de los botones para seleccionar el tipo de operacion a realizar
B_Operaciones = Button(root,text="Repaso Matematico", font = ("toms handwritten new",18), bg = "#ef7f74", command = lambda: mat.pantalla_Repaso(root))
B_Operaciones.place(x=200 , y=400, width=170, height=70)
#Boton Resta
B_Memorama = Button(root,text="Memorama", font = ("toms handwritten new",18), bg = "#ef7f74", command = Salir)
B_Memorama.place(x = 450,y = 400, width=130, height=70)
#Boton multiplicacion
B_ahorcado = Button(root, text="Ahorcado",font = ("toms handwritten new",18), bg = "#ef7f74", command= multi)
B_ahorcado.place(x = 650, y = 400, width=130, height=70)

#Boton salida
b_salir = Button(root, text = "Salir",font = ("toms handwritten new",18), bg = "#ef7f74", command = Salir)
b_salir.place(x = 800, y = 500, width=110, height=50)

root.mainloop()