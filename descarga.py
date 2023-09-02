import os
from pytube import YouTube

def download_video(url, filename):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res="480p").first()
        current_dir = os.getcwd()
        file_path = os.path.join(current_dir, filename)
        stream.download(filename=file_path)
        print(f"Descarga completada: {filename}")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")