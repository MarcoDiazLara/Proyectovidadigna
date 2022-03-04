from tkinter import *
import random

def crea_palabra():
    global palabra, palabra_aux
    palabra = valor.get()
    entrada.delete(0,END)
    num = len(palabra)
    palabra_aux = palabra
    fondo_tapa = Label(ventana, image = tapa, bg = "#26867d").place(x = 400, y = 500)
    
    for i in range (1,num):
        palabra_aux = palabra_aux.replace(palabra_aux[i], "*")
        
    L3 = Label(ventana, text = palabra_aux, fg = "White", bg = "#26867d", font = ("arial",25 ))
    L3.place(x = 400, y = 500)


def Comprobar():
    global palabra_aux
    res = letra.get()
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
    
    

def Salir_2():
    ventana.destroy()

def main(root):
    global ventana, valor, letra, entrada, tapa
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
    #Botones
    b_enviar = Button(ventana, text = "Enviar",font = ("arial",15), bg = "#ef7f74", command = crea_palabra)
    b_enviar.place(x = 210, y = 50, width=130, height=25)
    b_ingre = Button(ventana, text = "Enviar",font = ("arial",15), bg = "#ef7f74", command = Comprobar)
    b_ingre.place(x = 750, y = 280)
    b_salir = Button(ventana, text = "Salir",font = ("arial",18), bg = "#ef7f74", command = Salir_2)
    b_salir.place(x = 800, y = 500, width=110, height=50)
    
    ventana.mainloop()
