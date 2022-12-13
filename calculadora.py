from tkinter import *
from tkinter import filedialog as f
import math
from io import open

ventana =Tk()
ventana.title("Calculadora JHN")
ventana.resizable(0,0)
ventana.config(bg="Light gray")
i=0

etiqueta = Label (ventana, text=" La calculadora JHN")
etiqueta.pack
marco_principal= Frame()

marco_principal.config(bg="red")


e_texto = Entry(ventana,font= ("ARIAL 15"))
e_texto.grid(row =0, column=0, columnspan=5, padx=10, pady=10)

#funciones
def click_boton (valor):
    global i
    e_texto.insert(i,valor)
    i += 1 

def borrar():
    e_texto.delete(0,END)
    i = 0

def borrar_uno():
    global i
    e_texto.delete(i,END)
    i-=1

def operacion():
    global i
    ecuacion = e_texto.get()
    if i !=0:
        try:
            resultado = eval(ecuacion)
            e_texto.delete(0,END)
            e_texto.insert(0,resultado)
            i=0
        except:
            resultado ="ERROR"
            e_texto.delete(0,END)
            e_texto.insert(0,resultado)



#botones
boton1= Button (ventana, text="1", width=5, height=2, command=lambda:click_boton(1))
boton2= Button (ventana, text="2", width=5, height=2, command=lambda:click_boton(2))
boton3= Button (ventana, text="3", width=5, height=2, command=lambda:click_boton(3))
boton4= Button (ventana, text="4", width=5, height=2, command=lambda:click_boton(4))
boton5= Button (ventana, text="5", width=5, height=2, command=lambda:click_boton(5))
boton6= Button (ventana, text="6", width=5, height=2, command=lambda:click_boton(6))
boton7= Button (ventana, text="7", width=5, height=2, command=lambda:click_boton(7))
boton8= Button (ventana, text="8", width=5, height=2, command=lambda:click_boton(8))
boton9= Button (ventana, text="9", width=5, height=2, command=lambda:click_boton(9))

boton0= Button (ventana, text="0", width=15, height=2, command=lambda:click_boton(0))
botonsum= Button (ventana, text="+", width=5, height=2, command=lambda:click_boton("+"))
botonres= Button (ventana, text="-", width=5, height=2, command=lambda:click_boton("-"))
botonmul= Button (ventana, text="*", width=5, height=2, command=lambda:click_boton("*"))
botondiv= Button (ventana, text="/", width=5, height=2, command=lambda:click_boton("/"))
botoncoma= Button (ventana, text=",", width=5, height=2, command=lambda:click_boton(","))

boton_borrar= Button (ventana, text="AC", width=5, height=2, command=lambda:borrar())
boton_paren1= Button (ventana, text="(", width=5, height=2, command=lambda:click_boton("("))
boton_paren2= Button (ventana, text=")", width=5, height=2, command=lambda:click_boton(")"))
boton_igual= Button (ventana, text="=", width=5, height=2, command=lambda:operacion())

# boton_porcentaje= Button (ventana, text="%", width=5, height=2, command=lambda:click_boton("%"))
# boton_exponente= Button (ventana, text="^", width=5, height=2, command=lambda:click_boton("^"))
# boton_log= Button (ventana, text="Log", width=5, height=2, command=lambda:click_boton("log("))
# boton_ln= Button (ventana, text="ln", width=5, height=2, command=lambda:click_boton("ln("))
# boton_pi= Button (ventana, text="pi", width=5, height=2, command=lambda:click_boton("pi"))

#boton_seno= Button (ventana, text="seno", width=5, height=2, command=lambda:seno("seno"))

boton1.grid(row =4, column=0,  padx=5, pady=5)
boton2.grid(row =4, column=1,  padx=5, pady=5)
boton3.grid(row =4, column=2,  padx=5, pady=5)
boton4.grid(row =3, column=0,  padx=5, pady=5)
boton5.grid(row =3, column=1,  padx=5, pady=5)
boton6.grid(row =3, column=2,  padx=5, pady=5)
boton7.grid(row =2, column=0,  padx=5, pady=5)
boton8.grid(row =2, column=1,  padx=5, pady=5)
boton9.grid(row =2, column=2,  padx=5, pady=5)

boton0.grid(row =5, column=0, columnspan=2,  padx=5, pady=5)
botonsum.grid(row =4, column=3,  padx=5, pady=5)
botonres.grid(row =3, column=3,  padx=5, pady=5)
botonmul.grid(row =2, column=3,  padx=5, pady=5)
botondiv.grid(row =1, column=3,  padx=5, pady=5)
botoncoma.grid(row =5, column=2,  padx=5, pady=5)

boton_borrar.grid(row =1, column=0,  padx=5, pady=5)
boton_paren1.grid(row =1, column=1,  padx=5, pady=5)
boton_paren2.grid(row =1, column=2,  padx=5, pady=5)
boton_igual.grid(row =5, column=3,  padx=5, pady=5)

# boton_porcentaje.grid(row =1, column=4,  padx=5, pady=5)
# boton_exponente.grid(row =2, column=4,  padx=5, pady=5)
# boton_log.grid(row =3, column=4,  padx=5, pady=5)
# boton_ln.grid(row =4, column=4,  padx=5, pady=5)
# boton_pi.grid(row =5, column=4,  padx=5, pady=5)

#boton_seno.grid(row =5, column=3,  padx=5, pady=5)

ventana.mainloop()