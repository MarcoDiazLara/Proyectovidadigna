import matematicas as mat
import memorama as mem
import Ahorcado as Ahor
from tkinter import *
from tkinter import ttk
  

def Salir():
    root.destroy()
    
 
#Iniciacion de la interfaz grafica
root = Tk()
root.geometry("1000x600")
root.title("Sin nombre")
root["bg"] = "#26867d"
root.resizable(False,False)

#Colocacion del logo
imagen = PhotoImage(file = "Imagenes/Logo.png")
fondo = Label(root, image = imagen, bg = "#26867d" ).place(x = 400, y = 200)


#Creacion de los botones para seleccionar el tipo de operacion a realizar
B_Operaciones = Button(root,text="Repaso Matematico", font = ("toms handwritten new",18), bg = "#ef7f74", command = lambda: mat.pantalla_Repaso(root))
B_Operaciones.place(x=200 , y=400, width=170, height=70)
#Boton Resta
B_Memorama = Button(root,text="Memorama", font = ("toms handwritten new",18), bg = "#ef7f74", command = lambda: mem.main(root))
B_Memorama.place(x = 450,y = 400, width=130, height=70)
#Boton multiplicacion
B_ahorcado = Button(root, text="Ahorcado",font = ("toms handwritten new",18), bg = "#ef7f74", command = lambda: Ahor.main(root))
B_ahorcado.place(x = 650, y = 400, width=130, height=70)

#Boton salida
b_salir = Button(root, text = "Salir",font = ("toms handwritten new",18), bg = "#ef7f74", command = Salir)
b_salir.place(x = 800, y = 500, width=110, height=50)

root.mainloop()