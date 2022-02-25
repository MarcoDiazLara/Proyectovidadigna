from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MB
import random

def valores(llave):
    b_compro["state"] = NORMAL
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

def dib_signo():
    valor = combo.get()
    if valor == "Suma":
        #aux1 = signo_suma.subsample(1)
        fondo_tapa = Label(newWindow, image = tapa, bg = "#26867d").place(x = 300, y = 220)
        fondo_suma = Label(newWindow, image = signo_suma,bg = "#26867d").place(x = 300, y = 220) 
    elif valor == "Resta":
        fondo_tapa = Label(newWindow, image = tapa, bg = "#26867d").place(x = 300, y = 220)
        fondo_resta = Label(newWindow, image = signo_resta, bg = "#26867d").place(x = 300, y = 220)
    elif valor == "Multiplicacion":
        fondo_tapa = Label(newWindow, image = tapa, bg = "#26867d").place(x = 300, y = 220)
        fondo_multi = Label(newWindow, image = signo_multi, bg = "#26867d").place(x = 300, y = 220)
    else:
        MB.showwarning("Alerta", "Debes seleccionar una opcion valida")

def sel():
    valor = combo.get()
    global a,b
    if valor == "Suma":
        dib_signo()
        a,b = valores(1)
        aux1 = Label(newWindow,text = "     ", fg = "White", bg = "#26867d", font = ("arial",25 ) )
        aux1.place(x = 160 , y = 270)
        aux2 = Label(newWindow,text = "     ", fg = "White", bg = "#26867d", font = ("arial",25 ) )
        aux2.place(x = 560 , y = 270)
        L1S = Label(newWindow,text = str(a), fg = "White", bg = "#26867d", font = ("arial",25 ) )
        L1S.place(x = 160 , y = 270)
        L2S = Label(newWindow,text = str(b), fg = "White", bg = "#26867d", font = ("arial",25 ) )
        L2S.place(x = 560 , y = 270)
        
    elif valor == "Resta":
        a,b = valores(2)
        dib_signo()
        aux1 = Label(newWindow,text = "     ", fg = "White", bg = "#26867d", font = ("arial",25 ) )
        aux1.place(x = 160 , y = 270)
        aux2 = Label(newWindow,text = "     ", fg = "White", bg = "#26867d", font = ("arial",25 ) )
        aux2.place(x = 560 , y = 270)
        L1S = Label(newWindow,text = str(a), fg = "White", bg = "#26867d", font = ("arial",25 ) )
        L1S.place(x = 160 , y = 270)
        L2S = Label(newWindow,text = str(b), fg = "White", bg = "#26867d", font = ("arial",25 ) )
        L2S.place(x = 560 , y = 270)
    elif valor == "Multiplicacion":
        dib_signo()
        a,b = valores(3)
        aux1 = Label(newWindow,text = "     ", fg = "White", bg = "#26867d", font = ("arial",25 ) )
        aux1.place(x = 160 , y = 270)
        aux2 = Label(newWindow,text = "     ", fg = "White", bg = "#26867d", font = ("arial",25 ) )
        aux2.place(x = 560 , y = 270)
        L1S = Label(newWindow,text = str(a), fg = "White", bg = "#26867d", font = ("arial",25 ) )
        L1S.place(x = 160 , y = 270)
        L2S = Label(newWindow,text = str(b), fg = "White", bg = "#26867d", font = ("arial",25 ) )
        L2S.place(x = 560 , y = 270)
    else:
        MB.showwarning("Alerta", "Debes seleccionar una opcion valida")

def Salir_2():
    newWindow.destroy()
    
def Compro():
    resultado = int(res.get())
    llave = combo.get()
    if(llave == "Suma"): 
        if (resultado == (a+b)):
            MB.showinfo("Felicidades","Respuesta Correcta")
            sel()
        else:
            MB.showinfo("Error","Respuesta Incorrecta")
    elif(llave == "Resta"):
        if (resultado == (a-b)):
            MB.showinfo("Felicidades","Respuesta Correcta")
            sel()
        else:
            MB.showinfo("Error","Respuesta Incorrecta")
    elif(llave == "Multiplicacion"):
        if (resultado == (a*b)):
            MB.showinfo("Felicidades","Respuesta Correcta")
            sel()
        else:
            MB.showinfo("Error","Respuesta Incorrecta")


def pantalla_Repaso(root):
    #creacion de la nueva ventana
    
    global newWindow, bandera, fondo_suma, valor, b_start, b_compro, combo, res, signo_suma, signo_resta, tapa, signo_multi
    bandera = 0
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
    b_compro = Button(newWindow, text = "Comprobar", font = ("arial",15), bg = "#ef7f74", state = DISABLED, command = Compro)
    b_compro.place(x = 300, y = 500, width=150, height=80)
    #Boton salida
    b_salir = Button(newWindow, text = "Salir",font = ("arial",18), bg = "#ef7f74", command = Salir_2)
    b_salir.place(x = 800, y = 500, width=110, height=50)
    #signo_suma = PhotoImage(file = "Imagenes/mas.png")
    #fondo4 = Label(newWindow, image = signo_suma).place(x = 10, y = 20)
    signo_suma = PhotoImage(file = "Imagenes/mas.png")
    signo_suma = signo_suma.subsample(2)
    signo_resta = PhotoImage(file = "Imagenes/menos.png")
    signo_resta = signo_resta.subsample(7)
    tapa = PhotoImage(file = "Imagenes/tapa.png")
    tapa = tapa.subsample(2)
    signo_multi = PhotoImage(file = "Imagenes/multi.png")
    
    newWindow.mainloop()
    
