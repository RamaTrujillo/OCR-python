import os
import tkinter as tk
from tkinter import Toplevel
from threading import Thread
from tkinter.ttk import Progressbar
from contador import count_word_occurrences_in_video
from descarga import download_video


def download_and_count():
    url_entry.config(state=tk.DISABLED)
    word_entry.config(state=tk.DISABLED)
    download_button.config(state=tk.DISABLED)
    # Obtener la URL del video
    url = url_entry.get()
    # Obtener la ruta del directorio actual
    current_dir = os.path.dirname(__file__)
    # Concatenar la ruta con el nombre del archivo
    filename = os.path.join(current_dir, "Descarga.mp4")
    # Descargar el video en un hilo separado
    download = download_video(url, filename)
    if not download:
        error_window = tk.Toplevel(window)
        error_window.title("Error")
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - 200) // 2 
        y = (screen_height - 100) // 2
        error_window.geometry(f"200x100+{x}+{y}") 
        error_label = tk.Label(error_window, text='Error descargando el video', padx=10, pady=10)
        error_label.pack()
        error_button = tk.Button(error_window, text="Aceptar", command=error_window.destroy)
        error_button.pack()
        error_window.focus_force()
        error_window.grab_set()
        url_entry.config(state=tk.NORMAL)
        word_entry.config(state=tk.NORMAL)
        download_button.config(state=tk.NORMAL)

    # Mostrar el mensaje de carga
    if download:
        loading_label.config(text="Procesando video...")
        loading_label.pack()
        # Crear y mostrar el medidor de progreso
        progress_bar = Progressbar(window, orient=tk.HORIZONTAL, length=200, mode='indeterminate')
        progress_bar.pack(pady=10)
        progress_bar.start()
        # Contar la cantidad de veces que aparece la palabra en el video en un hilo separado
        word = word_entry.get()
        count_thread = Thread(target=count_occurrences, args=(filename, word, progress_bar))
        count_thread.start()

def count_occurrences(filename, word, progress_bar):
    occurrences = count_word_occurrences_in_video(filename, word)
    # Actualizar la etiqueta de resultado y detener el medidor de progreso
    result_label.config(text=f"La palabra '{word}' aparece {occurrences} segundos en el video.")
    result_label.pack(pady=10)
    progress_bar.stop()
    progress_bar.pack_forget()
    # Habilitar los inputs y el botón nuevamente
    url_entry.config(state=tk.NORMAL)
    word_entry.config(state=tk.NORMAL)
    download_button.config(state=tk.NORMAL)

# Crear la ventana principal
window = tk.Tk()
window.title("Contador de Palabras en Video")
window.geometry("400x300")

# Cambiar el estilo de la ventana
window.configure(bg='#F0F0F0')

# Crear los elementos de la interfaz
url_label = tk.Label(window, text="URL del video:", bg='#F0F0F0')
url_label.pack(pady=10)
url_entry = tk.Entry(window, width=40)
url_entry.pack()
word_label = tk.Label(window, text="Palabra a contar:", bg='#F0F0F0')
word_label.pack(pady=10)
word_entry = tk.Entry(window, width=40)
word_entry.pack()
download_button = tk.Button(window, text="Descargar y Contar", command=download_and_count, bg='#4CAF50', fg='white')
download_button.pack(pady=10)
loading_label = tk.Label(window, text="", bg='#F0F0F0')
result_label = tk.Label(window, text="", bg='#F0F0F0')

# Iniciar la ventana principal
window.mainloop()