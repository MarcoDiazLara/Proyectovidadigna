from tkinter import *
import random
from tkinter import messagebox as MB



def crea_palabra():
    global palabra, palabra_aux
    palabra = valor.get()
    entrada.delete(0,END)
    num = len(palabra)
    palabra_aux = palabra
    fondo_tapa = Label(ventana, image = tapa, bg = "#26867d").place(x = 400, y = 500)
    
    pal = list(palabra_aux)
    for i in range (1,num):
        pal[i] =  "*"
    palabra_aux = "".join(pal)
    
    L3 = Label(ventana, text = palabra_aux, fg = "White", bg = "#26867d", font = ("arial",25 ))
    L3.place(x = 400, y = 500)
    b_ingre["state"] = NORMAL

def Comprobar():
    global palabra_aux, conta 
    res = letra.get()
    entrada_letra.delete(0,END)
    if(palabra.find(res)>=0):
        aux = list(palabra)
        aux2 = list(palabra_aux)
        for i in range (0,len(palabra)):
            if(aux[i] == res):
                aux2[i] = res
        pal = "".join(aux2)
    
        palabra_aux = pal
        fondo_tapa = Label(ventana, image = tapa, bg = "#26867d").place(x = 400, y = 500)
        
        L3 = Label(ventana, text = pal, fg = "White", bg = "#26867d", font = ("arial",25 ))
        L3.place(x = 400, y = 500)
        if(palabra_aux == palabra):
            MB.showinfo("Felicidades!!","Acertaste la palabra, Ingresa una nueva palabra para continuar")
            reset()
        
    else:
        conta += 1
        if(conta == 1):
            fondo_2 = Label(ventana, image = inicio_2, bg = "#26867d").place(x = 300, y = 150)
        elif(conta == 2):
            fondo_2 = Label(ventana, image = inicio_3, bg = "#26867d").place(x = 300, y = 150)
        elif(conta == 3):
            fondo_2 = Label(ventana, image = inicio_4, bg = "#26867d").place(x = 300, y = 150)
        elif(conta == 4):
            fondo_2 = Label(ventana, image = inicio_5, bg = "#26867d").place(x = 300, y = 150)
        elif(conta == 5):
            fondo_2 = Label(ventana, image = inicio_6, bg = "#26867d").place(x = 300, y = 150)
        elif(conta == 6):
            fondo_2 = Label(ventana, image = inicio_7, bg = "#26867d").place(x = 300, y = 150)
        elif(conta == 7):
        
            MB.showinfo("Mala Suerte","Gastaste todos tus intentos :(, Ingresa una nueva palabra para continuar")
            reset()

def reset():
    fondo_inicio = Label(ventana, image = inicio, bg = "#26867d").place(x = 300, y = 150)
    fondo_tapa = Label(ventana, image = tapa, bg = "#26867d").place(x = 400, y = 500)
    b_ingre["state"] = DISABLED
    conta = 0

def Salir_2(root):
    root.deiconify()
    ventana.destroy()

def main(root):
    root.iconify()
    global ventana, valor, letra, entrada, tapa, entrada_letra, b_ingre, inicio
    global conta, inicio_2, inicio_3, inicio_4, inicio_5, inicio_6, inicio_7
    conta = 0
    ventana = Toplevel(root)
    ventana.geometry("1000x600")
    ventana.title("Ahorcado")
    ventana["bg"] = "#26867d"
    ventana.resizable(False,False)
    
    L1 = Label(ventana, text = "¿Cuál es la palabra a  utilizar?", fg = "White", bg = "#26867d", font = ("arial",18 ))
    L1.place(x = 10, y = 10)
    L2 = Label(ventana, text = "Ingresa la letra:", fg = "White", bg = "#26867d", font = ("arial",18 ))
    L2.place(x = 750, y = 180)
    valor = StringVar()
    entrada = Entry(ventana, textvariable = valor)
    entrada.place(x = 50, y = 50, width=150, height=25)
    letra = StringVar()
    entrada_letra = Entry(ventana, textvariable = letra, font = ("arial",18 ))
    entrada_letra.place(x = 750, y = 210,width=175, height=50)
    tapa = PhotoImage(file = "Imagenes/tapa_mem.png")
    tapa = tapa.subsample(3)
    inicio = PhotoImage(file = "Ahorcado/inicio.png")
    inicio_2 = PhotoImage(file = "Ahorcado/estado_2.png")
    inicio_3 = PhotoImage(file = "Ahorcado/estado_3.png")
    inicio_4 = PhotoImage(file = "Ahorcado/estado_4.png")
    inicio_5 = PhotoImage(file = "Ahorcado/estado_5.png")
    inicio_6 = PhotoImage(file = "Ahorcado/estado_6.png")
    inicio_7 = PhotoImage(file = "Ahorcado/estado_7.png")
    
    fondo_inicio = Label(ventana, image = inicio, bg = "#26867d").place(x = 300, y = 150)
    
    #Botones
    b_enviar = Button(ventana, text = "Enviar",font = ("arial",15), bg = "#ef7f74", command = crea_palabra)
    b_enviar.place(x = 210, y = 50, width=130, height=25)
    b_ingre = Button(ventana, text = "Ingresar",font = ("arial",15), bg = "#ef7f74", state = DISABLED, command = Comprobar)
    b_ingre.place(x = 750, y = 280)
    b_salir = Button(ventana, text = "Salir",font = ("arial",18), bg = "#ef7f74", command = lambda: Salir_2(root))
    b_salir.place(x = 800, y = 500, width=110, height=50)
    
    ventana.mainloop()

