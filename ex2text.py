from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

""" Funciones """

def buscar_archivo():
    """ declaramos la variable ruta como global para no tener que retornar nada
    e igualarla a la ruta del archivo seleccionado altiro"""
    global ruta
    buscar_archivo = askopenfilename(filetypes=(("Template files", "*.tplate"),("HTML files", "*.html;*.htm"),("All files", "*.*")))
    """ Igualamos la variable ruta a la ruta del archivo que se selecciono, ahora ruta no deja de ser un string vacio"""
    ruta = buscar_archivo
    """ en el entry ruta_origen insertamos el string de la ruta para que aparesca en el cuadro """
    ruta_origen.insert(0,ruta)
    return 0


""" los metodos o las funciones deben ir arriba del mainloop, lo mas ordenado es al principio,
cuando le pases el metodo o funcion al boton que quieres que ejecute coloca solo el nombre sin los parentesis(),
si no el interprete asume que le estas dando la orden que la ejecute, por eso se abria el cuadro de dialogo altiro. """

maestro = Tk()
maestro.geometry('790x300')

#sector de eleccion de archivos
frame_archivos       = LabelFrame(maestro , text="primer frame", pady=13)

#widgets de frame eleccion de archivos

""" Declaramos la variable ruta como un str vacio """

ruta = ""
texto_origen  = Label(frame_archivos,  text = "Seleccione Archivo")
texto_destino = Label(frame_archivos,  text = "Seleccione Destino")
""" Le decimos al entry que el texto que posea lo almacene en la variable ruta"""
ruta_origen   = Entry(frame_archivos,  width=50, textvariable=ruta)
ruta_destino  = Entry(frame_archivos,  width=50)

#este boton quisiera que invocara el metodo busqueda de archivos, pero no se como invocar el comando
boton_origen  = Button(frame_archivos, text = "origen", command= buscar_archivo)

boton_destino = Button(frame_archivos, text = "destino")

#distribucion de lugar de los wigets
frame_archivos.grid(row = 0 , column =0)
texto_origen.grid(row = 0 , column=0 )
ruta_origen.grid(row = 1 , column=0)
boton_origen.grid(row = 1 , column=1)
texto_destino.grid(row = 3 , column=0)
ruta_destino.grid(row = 4 , column=0)
boton_destino.grid(row = 4 , column=1)

#----------------------------------------------------------------------------------
#sector de tipo de libro
frame_tipoLibro = LabelFrame(maestro, text="Tipo libro", width=300, height=110,  padx=60, pady=5)

#widgets
combo_libros = ttk.Combobox(frame_tipoLibro)
combo_meses = ttk.Combobox(frame_tipoLibro)
combo_anios = ttk.Combobox(frame_tipoLibro)

texto_tipo_libro = Label(frame_tipoLibro,text="Seleccione Tipo de Libro")
texto_mes_salida = Label(frame_tipoLibro,text="Seleccione un Mes")
texto_anio_salida = Label(frame_tipoLibro,text="Seleccione un Anio")


#distribucion de los widgets
frame_tipoLibro.grid(row = 0 , column =1)
texto_tipo_libro.pack()
combo_libros.pack()
texto_mes_salida.pack()
combo_meses.pack()
texto_anio_salida.pack()
combo_anios.pack()

#valores de combos
combo_libros.config( values=('Libro_Diario','Libro_Mayor','Libro_Balance'))
combo_meses.config(values=('Enero','Feberero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'))
combo_anios.config(values=('2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'))

#----------------------------------------------------------------------------------
#sector de imagenes
frame_imagenes = LabelFrame(maestro, text="Imagenes", width=480, height=180)
#widgets


#distribucion de los widgets
frame_imagenes.grid(row = 1 , column =0)

#----------------------------------------------------------------------------------
#sector de comenzar
frame_comienzo_proceso = LabelFrame(maestro, text="Comienzo Proceso", padx=105, pady=50)
#widgets
boton_comenzar = Button(frame_comienzo_proceso,text="Comenzar")
#distribucion de los widgets
frame_comienzo_proceso.grid(row = 1 , column =1)
boton_comenzar.pack()

maestro.mainloop()
