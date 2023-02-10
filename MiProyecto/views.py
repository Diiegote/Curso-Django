from django.http import HttpResponse as response
import datetime

#Request: Para realizar peticiones.
# HtppResponse: Para enviar la respuesta usando el protocolo HTTP.

def bienvenida(request): #Pasamos un objeto de tipo request como primer argumento.
   return response("Bienvenidos a mi pagina")

def bienvenidaRojo(request): #Pasamos un objeto de tipo request como primer argumento.
   return response("<p style='color:red;font-size:5rem;'>Bienvenidos a mi pagina</p>")

def categoriaEdad(request,edad):
   if edad >= 18 :
      if edad >= 60:
         categoria = "Tercera edad"
      else:
         categoria = "Adultez"
   else:
      if edad <=10:
         categoria = "Infancia"
      else:
         categoria = "Adolecencia"
   resultado =f"<h1 style='color:green;font-size:3rem;'>Categoria de la edad: {categoria}</h1>"
   return response(resultado)   
         
         
def horaActual(request):
      respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
      return response(respuesta)