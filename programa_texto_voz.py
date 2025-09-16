# Texto a Voz
# La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible
# en formato mp3. Para ello puedes hacer uso de bibliotecas existentes como nltk, newspaper3k y gtts.
# Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para
# luego manejar la conversión de texto a voz.

import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from newspaper import Article
from gtts import gTTS
import os

def convertir_texto_a_voz(texto):
    if not texto.strip():
        print("No se proporcionó texto para convertir.")
        return
    tts = gTTS(text=texto, lang='es')
    archivo_audio = 'articulo.mp3'
    tts.save(archivo_audio)
    print(f"El texto ha sido convertido a audio y guardado como {archivo_audio}")

def obtener_texto_desde_url(url):
    try:
        articulo = Article(url)
        articulo.download()
        articulo.parse()
        return articulo.text
    except Exception as e:
        print(f"Error al obtener el artículo: {e}")
        return ""

def obtener_texto_desde_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return ""

if __name__ == "__main__":
    print("Opciones:")
    print("1. Convertir artículo desde URL")
    print("2. Escribir texto manualmente")
    print("3. Usar texto desde archivo local")
    opcion = input("Selecciona una opción (1/2/3): ").strip()

    texto = ""
    if opcion == "1":
        url = input("Introduce la URL del artículo: ")
        texto = obtener_texto_desde_url(url)
    elif opcion == "2":
        while True:
            print("Escribe el texto (finaliza con una línea vacía):")
            lineas = []
            while True:
                linea = input()
                if linea == "":
                    break
                lineas.append(linea)
            texto = "\n".join(lineas)

            if texto.strip():
                convertir_texto_a_voz(texto)
                reproducir = input("¿Quieres reproducir el audio? (s/n): ").strip().lower()
                if reproducir == "s":
                    os.system(f"start {os.path.abspath('articulo.mp3')}")
            else:
                print("No se proporcionó texto para convertir.")

            continuar = input("¿Quieres escribir otro texto? (s/n): ").strip().lower()
            if continuar != "s":
                break
    elif opcion == "3":
        ruta = input("Introduce la ruta del archivo de texto: ")
        texto = obtener_texto_desde_archivo(ruta)
    else:
        print("Opción no válida.")
        exit()

    if texto.strip():
        convertir_texto_a_voz(texto)
        reproducir = input("¿Quieres reproducir el audio? (s/n): ").strip().lower()
        if reproducir == "s":
            os.system(f"start {os.path.abspath('articulo.mp3')}")
    else:
        print("No se pudo obtener texto para convertir.")

