import cv2
import easyocr
import numpy as np  # Importa la biblioteca numpy para manipular imágenes

def count_word_occurrences_in_video(video_path, word_to_count, frames_per_second=1):
    reader = easyocr.Reader(['es'])
    cap = cv2.VideoCapture(video_path)
    word_occurrences = 0
    frame_count = 0
    # Obtener la tasa de cuadros por segundo del video
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Conjunto para realizar un seguimiento de los cuadros ya procesados
    processed_frames = set()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        # Procesar solo un fotograma cada frames_per_second segundos
        if frame_count % int(fps / frames_per_second) == 0:
            # Verificar si ya se ha procesado este cuadro
            frame_hash = hash(frame.tostring())
            if frame_hash not in processed_frames:
                # Realizar el OCR en el cuadro actual
                detected_text = reader.readtext(frame)
                
                # Verificar si la palabra buscada aparece en el cuadro actual
                for detection in detected_text:
                    text = detection[1].lower()
                    if word_to_count.lower() in text:
                        # Si se encuentra la palabra, incrementar el recuento
                        word_occurrences += 1
                        
                        # Obtener las coordenadas del cuadro de texto
                        top_left = tuple(map(int, detection[0][0]))
                        bottom_right = tuple(map(int, detection[0][2]))
                        
                        # Dibujar un recuadro de color alrededor del texto
                        color = (0, 0, 255)  # Color en formato BGR (rojo en este caso)
                        thickness = 2  # Grosor del recuadro
                        cv2.rectangle(frame, top_left, bottom_right, color, thickness)
                
                processed_frames.add(frame_hash)  # Agregar el hash del cuadro a los cuadros procesados
            
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    cap.release()
    cv2.destroyAllWindows()
    return word_occurrences
