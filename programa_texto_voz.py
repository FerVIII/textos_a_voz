# Texto a Voz Avanzado
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

from newspaper import Article
from gtts import gTTS
import os
import platform
import subprocess

def reproducir_audio(ruta):
    if not os.path.exists(ruta):
        print(f"El archivo {ruta} no existe.")
        return
    
    sistema = platform.system()
    try:
        if sistema == "Windows":
            os.startfile(ruta)
        elif sistema == "Darwin":  # macOS
            subprocess.run(["open", ruta])
        else:  # Linux / WSL
            subprocess.run(["xdg-open", ruta])
    except Exception as e:
        print(f"No se pudo reproducir automáticamente: {e}")

def convertir_texto_a_voz(texto, ruta_archivo):
    if not texto.strip():
        print("No se proporcionó texto para convertir.")
        return False

    try:
        tts = gTTS(text=texto, lang='es')
        tts.save(ruta_archivo)
        print(f"Audio generado en: {ruta_archivo}")
        return True
    except Exception as e:
        print(f"Error al generar el audio: {e}")
        return False

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

def pedir_texto():
    print("Opciones:")
    print("1. Convertir artículo desde URL")
    print("2. Escribir texto manualmente")
    print("3. Usar texto desde archivo local")
    opcion = input("Selecciona una opción (1/2/3): ").strip()

    if opcion == "1":
        url = input("Introduce la URL del artículo: ")
        return obtener_texto_desde_url(url)
    elif opcion == "2":
        print("Escribe el texto (finaliza con una línea vacía):")
        lineas = []
        while True:
            linea = input()
            if linea == "":
                break
            lineas.append(linea)
        return "\n".join(lineas)
    elif opcion == "3":
        ruta = input("Introduce la ruta del archivo de texto: ")
        return obtener_texto_desde_archivo(ruta)
    else:
        print("Opción no válida.")
        return ""

if __name__ == "__main__":
    texto = pedir_texto()
    if texto.strip():
        ruta = input("Introduce el nombre o ruta del archivo de audio (ej: mi_audio.mp3 o ./audios/mi_audio.mp3): ").strip()
        if not ruta.endswith(".mp3"):
            ruta += ".mp3"
        
        if convertir_texto_a_voz(texto, ruta):
            reproducir_audio(ruta)
    else:
        print("No se pudo obtener texto para convertir.")
