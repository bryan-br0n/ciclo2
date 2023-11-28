#de 'decouple' importamos 'config'
from decouple import config
import requests
#realizamos la importacion de la utilidad
from Util.utilidades import traducir_texto
API_KEY = config('API_KEY')

def obtener_clima(ubicacion):
    if (ubicacion == None):
        return None
    
    # creamos ls variable url para realizar petición a la API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ubicacion}&appid={API_KEY}&units=metric"
    try:
        # creamos una variable para obtener el resultado de la API
        respuesta = requests.get(url)
        # creamos una variable para convertir el texto plano en un formato de .json (JavaScript Object Notation)
        datos_clima = respuesta.json()

        # crear nuestras variables que almacenaras los datos a mostrar
        temperatura = datos_clima["main"]["temp"]
        temp_maxima = datos_clima["main"]["temp_max"]
        temp_minima = datos_clima["main"]["temp_min"]
        descripcion_tiempo = datos_clima["weather"][0]["description"]
        humedad = datos_clima["main"]["humidity"]
        velocidad_viento = datos_clima["wind"]["speed"]

        mensaje = f"El clima en {ubicacion} es el siguiente:"
        mensaje += f"- Temperatura: {temperatura}"
        mensaje += f"- Temperatura maxima: {temp_maxima}"
        mensaje += f"- Temperatura minima: {temp_minima}"
        mensaje += f"- Descripción: {traducir_texto(descripcion_tiempo)}"
        mensaje += f"- Humedad: {humedad}%"
        mensaje += f"- Velocidad del viento: {velocidad_viento}"

        return mensaje
    except:
        return None