# Contador de Palabras en cada segundo del Video

Este proyecto es un contador de palabras en un video utilizando reconocimiento óptico de caracteres (OCR). Permite descargar un video de YouTube, procesarlo y contar cuántas segundos aparece una palabra específica en el video.

## Requisitos

- Python 3.x
- Librerías: pytube3, easyocr, opencv-python-headless, numpy

## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual e instala las dependencias utilizando el archivo  `requirements.txt` :
python -m venv nombre_entorno
source nombre_entorno/bin/activate (en macOS/Linux) o nombre_entorno\Scripts\activate (en Windows)
pip install -r requirements.txt
## Uso

1. Ejecuta el archivo  `index.pyw` .
2. Ingresa la URL del video de YouTube que deseas procesar.
3. Ingresa la palabra que deseas contar en el video.
4. Haz clic en el botón "Descargar y Contar".
5. El programa descargará el video en un hilo separado y comenzará a procesarlo en busca de la palabra especificada.
6. Una vez completado el procesamiento, se mostrará el resultado en la interfaz de usuario.

## Archivos

-  `index.pyw` : Contiene la interfaz gráfica de usuario y la lógica principal del programa.
-  `descarga.py` : Contiene la función para descargar el video de YouTube utilizando la librería pytube3.
-  `contador.py` : Contiene la función para contar la cantidad de veces que aparece una palabra en el video utilizando OCR con la librería easyocr y OpenCV.


## Créditos

Este proyecto fue creado por [Ramiro Trujillo](https://www.linkedin.com/in/ramiro-trujillo-b0775b202/) como parte del Trabajo práctico final para la carrera Técnico Superior En Desarrollo de Software.

## Licencia

Este proyecto está bajo la Licencia GPL.
