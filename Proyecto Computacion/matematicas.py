from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MB
import random

def valores(llave):
    if llave == 1:
        llave_suma = True
        while(llave_suma):
            A = random.randint(0,int(valor.get()))
            B = random.randint(0,int(valor.get()))
            if((A+B)<int(valor.get())):
                llave_suma = False
        return A,B
    elif llave == 2:
        llave_resta = True
        while(llave_resta):
            A = random.randint(0,int(valor.get()))
            B = random.randint(0,int(valor.get()))
            if((A-B)<int(valor.get()))& ((A-B)>=0):
                llave_resta = False
        return A,B
    elif llave == 3:
        llave_multi = True
        while(llave_multi):
            A = random.randint(0,int(valor.get()))
            B = random.randint(0,int(valor.get()))
            if((A*B)<int(valor.get())):
                llave_multi = False
        return A,B
    

def send():
    global num_A
    num_A = int(valor.get())
    b_start["state"] = NORMAL

def sel():
    valor = combo.get()
    if valor == "Suma":
        a,b = valores(1)
        print(a,b)
    elif valor == "Resta":
        a,b = valores(2)
        print(a,b)
    elif valor == "Multiplicacion":
        a,b = valores(3)
        print(a,b)
    else:
        MB.showwarning("Alerta", "Debes seleccionar una opcion valida")

def Salir_2():
    newWindow.destroy()
    

def pantalla_Repaso(root):
    #creacion de la nueva ventana
    
    global newWindow
    newWindow = Toplevel(root)
    newWindow.geometry("1000x600")
    newWindow.title("Repaso Matematico")
    newWindow["bg"] = "#26867d"
    newWindow.resizable(False,False)
    #Mandamos los globos a la pantalla
    globo1 = PhotoImage(file = "Imagenes/Globo1.png")
    globo12 = globo1.subsample(3)
    fondo1 = Label(newWindow, image = globo12,bg = "#26867d").place(x = 130, y = 230)
    
    globo2 = PhotoImage(file = "Imagenes/Globo2.png")
    globo22 = globo2.subsample(3)
    fondo2 = Label(newWindow, image = globo22, bg = "#26867d").place(x = 530, y = 230)
    #Colocacion de los signos
    signo_igual = PhotoImage(file = "Imagenes/igual.png")
    signo_igual2 = signo_igual.subsample(4)
    fondo3 = Label(newWindow, image = signo_igual2,bg = "#26867d").place(x = 700 , y = 220)
    
    L1 = Label(newWindow, text = "¿Cuál es el mayor número que conoce el alumno?", fg = "White", bg = "#26867d", font = ("arial",18 ))
    L1.place(x = 10, y = 10)
    L2 = Label(newWindow, text = "Operacion:", fg = "White", bg = "#26867d", font = ("arial",18 ))
    L2.place(x = 550, y = 50)
    
    
    
    #Entradas de texto
    global valor, b_start, b_compro, combo
    valor = StringVar()
    entrada = Entry(newWindow, textvariable = valor)
    entrada.place(x = 50, y = 50, width=130, height=25)
    res = Entry(newWindow, font = ("arial",35 ))
    res.place(x = 850, y = 230, width=120, height=100)
    #Creacion del Combobox
    combo = ttk.Combobox(newWindow, values = [ "Suma", "Resta", "Multiplicacion"],state = "readonly")
    combo.place(x = 680, y = 55, width = 130, height = 25)
    #Boton para comenzar
    b_start = Button(newWindow, text = "Comenzar",font = ("arial",15), bg = "#ef7f74", state = DISABLED, command = sel)
    b_start.place(x = 820, y = 55, width=130, height=25)
    #Boton para recibir el numero
    b_enviar = Button(newWindow, text = "Enviar",font = ("arial",15), bg = "#ef7f74", command = send)
    b_enviar.place(x = 210, y = 50, width=130, height=25)
    #Boton para evaluar el resultado
    b_compro = Button(newWindow, text = "Comprobar", font = ("arial",15), bg = "#ef7f74", state = DISABLED, command = Salir_2)
    b_compro.place(x = 300, y = 500, width=150, height=80)
    #Boton salida
    b_salir = Button(newWindow, text = "Salir",font = ("arial",18), bg = "#ef7f74", command = Salir_2)
    b_salir.place(x = 800, y = 500, width=110, height=50)
    #signo_suma = PhotoImage(file = "Imagenes/mas.png")
    #fondo4 = Label(newWindow, image = signo_suma).place(x = 10, y = 20)    
    
    newWindow.mainloop()
    
