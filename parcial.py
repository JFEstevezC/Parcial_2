from tkinter import *
import random

#ventana principal

#se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Generador de matriz")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="white")

m = StringVar()
b = StringVar()


frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "green", width = 480 , height = 480)
frame_entrada.place(x = 10, y = 10)

lb_m = Label(frame_entrada, text = "Tamaño: ")
lb_m.config(bg="green", fg="white", font=("Arial",16))
lb_m.place(x=10, y=10, width=115, height=30)

entry_m = Entry(frame_entrada, textvariable=m)
entry_m.config(font=("Arial",20), justify=LEFT,fg="black")
entry_m.focus_set()
entry_m.place(x=130, y=10, width=115, height=30)

lb_b = Label(frame_entrada, text = "Buscar: ")
lb_b.config(bg="green", fg="white", font=("Arial",16))
lb_b.place(x=250, y=10, width=115, height=30)

entry_b = Entry(frame_entrada, textvariable=b)
entry_b.config(font=("Arial",20), justify=LEFT,fg="black")
entry_b.focus_set()
entry_b.place(x=370, y=10, width=100, height=30)


def crear():
    ventana_sec = Toplevel()
    ventana_sec.title("MATRIZ")
    ventana_sec.geometry("400x400")
    ventana_sec.config(bg="green")
    frame_resultados = Frame(ventana_sec)
    frame_resultados.config(bg="white", width=930, height=480)
    frame_resultados.place(x=10, y = 10)
    t_resultados = Text(frame_resultados)
    t_resultados.config(bg="green", fg="black", font=("Arial",10))
    t_resultados.place(x=10,y=10, width=910, height= 400)
    M = []

    for i in range(m):
        M.append([])
    for j in range(n):
        M[i].append(random.randint(1,9))

    # Mostrar matriz
    for k in range(m):
        print()
    for j in range(n):
        print(M[k][j], end= "\t")


    def salir():
        ventana_sec.destroy()
    salir_btn =Button(ventana_sec, text="Salir de la ventana", command=exit, width="30", height="2")
    salir_btn.place(x=360, y=435)
    

bt_ejecutar = Button(frame_entrada, text="Crear la matriz", command=crear)
bt_ejecutar.place(x=70, y=440, width=100, height=30)

bt_buscar = Button(frame_entrada, text="Buscar numero: ")
bt_buscar.place(x=300, y=440, width=100, height=30)

# Dimensiones de la matriz
n = m



ventana_principal.mainloop()