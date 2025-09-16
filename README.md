# Texto a Voz 🗣️🎵

## Descripción

Este proyecto permite convertir un artículo, texto manual o archivo de texto en un archivo de audio reproducible en formato MP3. Utiliza librerías como `nltk`, `newspaper3k` y `gtts` para obtener, procesar y convertir texto a voz en español.

El objetivo es transformar artículos web o texto propio en audio para escuchar de manera sencilla.

---

## Captura previa

![Interfaz del proyecto](images/imagen_1.png)
![Interfaz del proyecto](images/imagen_2.png)
![Interfaz del proyecto](images/imagen_3.png)

---

## Tecnologías usadas

- Python 3.12
- [NLTK](https://www.nltk.org/) → procesamiento de texto
- [newspaper3k](https://newspaper.readthedocs.io/) → extracción de artículos web
- [gTTS](https://pypi.org/project/gTTS/) → conversión de texto a voz
- [Tkinter](https://docs.python.org/3/library/tkinter.html) → interfaz gráfica

---

## Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/FerVIII/pasar_texto_a_voz.git
cd pasar_texto_a_voz
```

2. Usar Conda (recomendado)

conda create -n portafolio python=3.12 -y
conda activate portafolio

3. Instalar librerías necesarias

pip install nltk newspaper3k gtts lxml[html_clean] Pillow

4. Descargar recursos de NLTK

python -c "import nltk; nltk.download('punkt')"

Uso

Al ejecutar el programa, se presentan tres opciones:

Convertir artículo desde URL

Introduce la URL de un artículo web.

El programa descargará el texto y generará un archivo articulo.mp3.

Escribir texto manualmente

Escribe tu texto directamente en la consola (finaliza con línea vacía).

Se genera un archivo articulo.mp3.

Opción de reproducir el audio automáticamente.

Usar texto desde archivo local

Introduce la ruta de un archivo .txt.

Se genera un archivo articulo.mp3.
