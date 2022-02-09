from tkinter import *
from playsound import playsound
from tkinter import messagebox
import random

class Carta:
	def __init__(self):
		self.valor = 0
		self.posicion = 0
		self.oculto = True
		self.foto = PhotoImage(file="memoria/fondo.gif")

class Memorama:
	def __init__(self):
		self.ventana = Toplevel(ven)
		self.ventana.title("memoria/memorama")
		self.ventana.geometry("1000x600")
		self.botones = []
		self.cartas = []
		self.temporal = Carta()
		self.a = 0
		self.par = 0
		self.listo = True
		self.fondo = PhotoImage(file="memoria/fondo.gif")
		self.creartablero()
		self.revolver()
		self.ventana.mainloop()

	def creartablero(self):
		i = 0
		contador = 0
		while i<4:
			j = 0
			while j<7:
				btn= Button(self.ventana,command=lambda a = contador:self.revisar(a), height=80,width=80,image=self.fondo)
				btn.place(x=(j+1)*90, y=(i+1)*90)
				self.botones.append(btn)
				j+=1
				contador+=1
			i+=1

		print("")

	def revolver(self):
		i = 1
		while (i<15):
			carta1 = Carta()
			carta1.valor = i
			carta1.foto = PhotoImage(file="memoria/"+str(i)+".gif")
			carta2 = Carta()
			carta2.valor = i
			carta2.foto = PhotoImage(file="memoria/"+str(i)+".1.gif")
			self.cartas.append(carta1)
			self.cartas.append(carta2)
			i+=1
		cartasTemporal = []
		while len(self.cartas)>0:
			posicion = random.randrange(0,len(self.cartas))
			cartasTemporal.append(self.cartas.pop(posicion))
		self.cartas = cartasTemporal

	def revisar(self,a):
		if self.listo == True and self.cartas[a].oculto==True:
			self.botones[a].config(image=self.cartas[a].foto)
			if self.par == 0:
				self.temporal = self.cartas[a]
				self.cartas[a].oculto = False
				self.temporal.posicion = a
				self.par = 1
			elif self.par==1:
				self.par = 0
				if self.temporal.valor == self.cartas[a].valor:
					self.cartas[a].oculto = False
					bandera = True
					
					for elemento in self.cartas:
						if elemento.oculto == True:
							bandera = False
							break
					if bandera == True:
						messagebox.showinfo("Ganaste","Felicidades, Ganaste")
				else:
					
					self.a = a
					self.listo = False
					self.ventana.after(1500,self.tapar)
					

	def tapar(self):
		self.cartas[self.temporal.posicion].oculto = True
		self.botones[self.temporal.posicion].config(image=self.fondo)
		self.botones[self.a].config(image=self.fondo)
		self.listo = True

def main(newWindow):
    global ven
    ven = newWindow
    obj = Memorama()
