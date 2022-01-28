import random
import os
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

def send():
    global num_A
    num_A = int(valor.get())
    b_multi["state"] = NORMAL
    b_suma["state"] = NORMAL
    b_resta["state"] = NORMAL

def Salir():
    root.destroy()

def pantalla_Repaso():
    #Deshabilitacion de botones
    B_Operaciones["state"] = DISABLED
    B_Memorama["state"] = DISABLED
    B_ahorcado["state"] = DISABLED
    #creacion de la nueva ventana
    global newWindow
    newWindow = Toplevel(root)
    newWindow.geometry("1000x600")
    newWindow.title("Repaso Matematico")
    newWindow["bg"] = "#26867d"
    
    L1 = Label(newWindow, text = "¿Cuál es el mayor número que conoce el alumno?", fg = "White", bg = "#26867d", font = ("arial",18 ))
    L1.place(x = 10, y = 10)
    L2 = Label(newWindow, text = "Operacion:", fg = "White", bg = "#26867d", font = ("arial",18 ))
    L2.place(x = 550, y = 50)
    
    #Mandamos los globos a la pantalla
    globo1 = PhotoImage(file = "Imagenes/Globo1.png")
    fondo1 = Label(root, image = globo1).place(x = 20, y = 30)
    """globo2 = PhotoImage(file = "Imagenes/Globo2.png")
    fondo2 = Label(newWindow, image = globo2).place(x = 200, y = 30)"""
    
    entrada = Entry(newWindow)
    entrada.place(x = 50, y = 50, width=130, height=25)
    
    combo = ttk.Combobox(newWindow, values = [ "Suma", "Resta", "Multiplicacion"])
    combo.place(x = 680, y = 55, width = 130, height = 25)
    
    b_enviar = Button(newWindow, text = "Enviar",font = ("arial",15), bg = "#ef7f74", command = Salir_2)
    b_enviar.place(x = 210, y = 50, width=130, height=25)
    #Boton salida
    b_salir = Button(newWindow, text = "Salir",font = ("arial",18), bg = "#ef7f74", command = Salir_2)
    b_salir.place(x = 800, y = 500, width=110, height=50)

def Salir_2():
    newWindow.destroy()
    B_Operaciones["state"] = NORMAL
    B_Memorama["state"] = NORMAL
    B_ahorcado["state"] = NORMAL
    
    
 
#Iniciacion de la interfaz grafica
root = Tk()
root.geometry("1000x600")
root.title("Practica Profesional")
root["bg"] = "#26867d"
#Entrada del valor mas alto que conoce el alumno
valor = StringVar()
Num = Entry(root, textvariable = valor)
Num.place(x=15,y=25,width=70, height=25)

#Colocacion del logo
imagen = PhotoImage(file = "Imagenes/Logo.png")
fondo = Label(root, image = imagen, bg = "#26867d" ).place(x = 400, y = 200)


#Creacion de los botones para seleccionar el tipo de operacion a realizar

B_Operaciones = Button(root,text="Repaso Matematico", font = ("toms handwritten new",18), bg = "#ef7f74", command = pantalla_Repaso)
B_Operaciones.place(x=200 , y=400, width=170, height=70)
#Boton Resta
B_Memorama = Button(root,text="Memorama", font = ("toms handwritten new",18), bg = "#ef7f74", command = resta)
B_Memorama.place(x = 450,y = 400, width=130, height=70)
#Boton multiplicacion
B_ahorcado = Button(root, text="Ahorcado",font = ("toms handwritten new",18), bg = "#ef7f74", command= multi)
B_ahorcado.place(x = 650, y = 400, width=130, height=70)

#Boton salida
b_salir = Button(root, text = "Salir",font = ("toms handwritten new",18), bg = "#ef7f74", command = Salir)
b_salir.place(x = 800, y = 500, width=110, height=50)

root.mainloop()