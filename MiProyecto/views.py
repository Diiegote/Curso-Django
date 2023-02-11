from django.http import HttpResponse as response
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

# Request: Para realizar peticiones.
# HtppResponse: Para enviar la respuesta usando el protocolo HTTP.


# Pasamos un objeto de tipo request como primer argumento.
def bienvenida(request):
    return response("Bienvenidos a mi pagina")


# Pasamos un objeto de tipo request como primer argumento.
def bienvenidaRojo(request):
    return response("<p style='color:red;font-size:5rem;'>Bienvenidos a mi pagina</p>")


def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "Adultez"
    else:
        if edad <= 10:
            categoria = "Infancia"
        else:
            categoria = "Adolecencia"
    resultado = f"<h1 style='color:green;font-size:3rem;'>Categoria de la edad: {categoria}</h1>"
    return response(resultado)


def horaActual(request):
    respuesta = "<h1>Momento actual: {0}</h1>".format(
        datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return response(respuesta)

 # manera no optima de realizar una plantilla


def contenidoHTML(request, nombre, edad):
    contenido = f"""
   <html>
   <body>
   <p>Nombre: {nombre}  Edad: {edad}</p>
   </body>
   </html>
   """
    return response(contenido)

 # Realizando una plantilla


def miPrimeraPlantilla(request):
    # abrimos el documento que contiene la plantilla:
    plantillaExterna = open(
        "C:/MiProyecto/MiProyecto/Plantillas/miPrimeraPlantilla.html")
    # cargar el documento en una variable de tipo 'Template'
    template = Template(plantillaExterna.read())
    # cerrar el documento externo que hemos abierto:
    plantillaExterna.close()
    # Crear un contexto
    contexto = Context()
    # Renderizamos el documento
    documento = template.render(contexto)
    return response(documento)

# Realizando una plantilla con parametros


def plantillaParametros(request):
    nombre = "Diego Martinotti"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "JavaScript", "Java",
                 "C#", "Ruby", "C++", "Kotlin", "PHP"]
    # abrimos el documento que contiene la plantilla:
    plantillaExterna = open(
        "C:/MiProyecto/MiProyecto/Plantillas/plantillaParametros.html")
    # cargar el documento en una variable de tipo 'Template'
    template = Template(plantillaExterna.read())
    # cerrar el documento externo que hemos abierto:
    plantillaExterna.close()
    # Crear un contexto
    contexto = Context(
        {"NombreCanal": nombre, "FechaActual": fechaActual, "Lenguajes": lenguajes})
    # Renderizamos el documento
    documento = template.render(contexto)
    return response(documento)

# Cargando plantillas con Loader (Manera OPTIMA de cargar plantillas)


def plantillaLoader(request):
    nombre = "Diego Martinotti"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "JavaScript", "Java",
                 "C#", "Ruby", "C++", "Kotlin", "PHP"]
    # Especificamos la carpeta donde se encuentra la plantilla y creamos una variable para almacenarla
    # La otra parte de la ruta esta configurada en settings
    plantillaExterna = loader.get_template("plantillaParametros.html")
    # Renderizamos el documento
    documento = plantillaExterna.render(
        {"NombreCanal": nombre, "FechaActual": fechaActual, "Lenguajes": lenguajes})
    return response(documento)

# Usando el metodo render que simplifica las cosas. Acepta como parametros obligatorios el objeto request, y el nombre de la plantilla, como parametros opcionales acepta un diccionario
def plantillaShortcuts(request):
    nombre = "Diego Martinotti"
    fechaActual = datetime.datetime.now()
    lenguajes = ["Python", "JavaScript", "Java",
                 "C#", "Ruby", "C++", "Kotlin", "PHP"]
    return render(request, "plantillaParametros.html", {"NombreCanal": nombre, "FechaActual": fechaActual, "Lenguajes": lenguajes})

# Usando Herencia de plantillas
def plantillaHija1(request):
   return render(request, "plantillaHija_1.html")

def plantillaHija2(request):
   return render(request, "plantillaHija_2.html")