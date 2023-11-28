# importar la libreria de google para traducir el texto
from googletrans import Translator

#crear una funcion para traducir texto
def traducir_texto(texto, idioma_origen="en", idioma_destino="es"):
    #creamos una instancia del objeto importado "Translator"
    translator = Translator()
    #obtenemos el resultado usando el metodo traslate
    resultado = translator.translate(texto, idioma_destino, idioma_origen)
    return resultado.text