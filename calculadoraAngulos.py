from tkinter import *
from math import *

#Funciones basicas
def magnitud_vector(vector:list):
    magnitud = 0
    for i in vector:
        magnitud = magnitud + (i**2)
    return sqrt(magnitud)

def producto_punto(vector1:list, vector2:list):
    suma = 0
    for i in range(len(vector1)):
        suma = suma + (vector1[i]*vector2[i])
    return suma

def funcion_resultado(vector1:list, vector2:list):
    mag_1 = magnitud_vector(vector1)
    mag_2 = magnitud_vector(vector2)
    multi = round(mag_1*mag_2, 5)
    pp = round(producto_punto(vector1, vector2),5)
    radian = round(acos((pp)/(multi)) * (180/pi),2)
    return radian

def funcion_cruz(vector1:list, vector2:list):
    cadena = f'({(vector1[1]*vector2[2])-(vector1[2]*vector2[1])}, {-((vector1[0]*vector2[2])-(vector2[0]*vector1[2]))}, {(vector1[0]*vector2[1])-(vector2[0]*vector1[1])})'
    return cadena
#Ventana
ventana = Tk()
ventana.title('Calculadora de resultado entre 2 vectores')
ventana.geometry('400x260')
ventana.resizable(width=0, height=0)




#Etiquetas
etiqueta1 = Label(ventana, text = 'Introduce los valores del primer vector.', font='Helvetica 10 bold')
etiqueta1.grid(column=0, row = 0)

etiqueta2 = Label(ventana, text = 'Introduce los valores del segundo vector.', font='Helvetica 10 bold')
etiqueta2.grid(column=0, row= 3)

a1 = Label(ventana, text = 'x', font='Helvetica 10 bold')
a1.grid(column =1, row = 1)

b2 = Label(ventana, text = 'y', font='Helvetica 10 bold')
b2.grid(column =2, row = 1)

b3 = Label(ventana, text = 'z', font='Helvetica 10 bold')
b3.grid(column =3, row = 1)


a1 = Label(ventana, text = 'x', font='Helvetica 10 bold')
a1.grid(column =1, row = 4)

b2 = Label(ventana, text = 'y', font='Helvetica 10 bold')
b2.grid(column =2, row = 4)

b3 = Label(ventana, text = 'z', font='Helvetica 10 bold')
b3.grid(column =3, row = 4)

resultado = Label(ventana, text = '', font='Helvica 12 bold')
resultado.grid(column = 0, row = 10)

#Entradas
v1x = Entry(ventana,width=5, bg="orange", font= 'Helvetica 10 bold', justify = 'center')
v1x.grid(column=1, row = 2)

v1y = Entry(ventana,width=5, bg="orange", font= 'Helvetica 10 bold', justify = 'center')
v1y.grid(column=2, row = 2)

v1z = Entry(ventana,width=5, bg="orange", font= 'Helvetica 10 bold', justify = 'center')
v1z.grid(column=3, row = 2)

v2x = Entry(ventana,width=5, bg="orange", font= 'Helvetica 10 bold', justify = 'center')
v2x.grid(column=1, row = 5)

v2y = Entry(ventana,width=5, bg="orange", font= 'Helvetica 10 bold', justify = 'center')
v2y.grid(column=2, row = 5)

v2z = Entry(ventana,width=5, bg="orange", font= 'Helvetica 10 bold', justify = 'center')
v2z.grid(column=3, row = 5)



#Funciones Boton
def calcular_angulo():
    
    try:
        vector1 = [int(v1x.get()), int(v1y.get()), int(v1z.get())]
        vector2 = [int(v2x.get()), int(v2y.get()), int(v2z.get())]
        radian = funcion_resultado(vector1, vector2)
        resultado.configure(text = f'α = {radian}°')
        
    except Exception as e:

        resultado.configure(text='ERROR!, ingrese bien los datos.')


def calcular_producto_punto():
    try:
        vector1 = [int(v1x.get()), int(v1y.get()), int(v1z.get())]
        vector2 = [int(v2x.get()), int(v2y.get()), int(v2z.get())]
        pp = producto_punto(vector1, vector2)
        resultado.configure(text=f'A·B = {pp}')
    except:
        resultado.configure(text='ERROR!, ingrese bien los datos.')

def calcular_producto_cruz():
    try:
        vector1 = [int(v1x.get()), int(v1y.get()), int(v1z.get())]
        vector2 = [int(v2x.get()), int(v2y.get()), int(v2z.get())]
        cadena = funcion_cruz(vector1, vector2)
        resultado.configure(text=f'AxB = {cadena}')        
    except :
        resultado.configure(text='ERROR!, ingrese bien los datos.')
#Botones
btn_calcular1 = Button(ventana, text="CALCULAR resultado", command=calcular_angulo, bg="yellow", font = 'Helvica 11 bold')
btn_calcular1.grid(column =0, row = 7, sticky= 'NS')

btn_calcular2 = Button(ventana, text="CALCULAR PRODUCTO PUNTO", command=calcular_producto_punto, bg="yellow", font = 'Helvica 11 bold')
btn_calcular2.grid(column =0, row = 8, sticky= 'NS')

btn_calcular2 = Button(ventana, text="CALCULAR PRODUCTO CRUZ", command=calcular_producto_cruz, bg="yellow", font = 'Helvica 11 bold')
btn_calcular2.grid(column =0, row = 9, sticky= 'NS')

#Ejecución de la  ventana
ventana.mainloop()


