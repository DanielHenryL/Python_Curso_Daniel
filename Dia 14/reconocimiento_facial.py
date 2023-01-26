import cv2
import face_recognition as fr

# Cargar imagenes
foto_control = fr.load_image_file('Foto B.jpeg')
foto_prueba = fr.load_image_file('Foto F.jpg')

# pasar imagenes a RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# Localizar cara prueba
lugar_cara_D = fr.face_locations(foto_prueba)[0]
cara_codificada_D = fr.face_encodings(foto_prueba)[0]

# Mostrar rectangulos
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]),
              (lugar_cara_A[1],lugar_cara_A[2]),
              (0, 255, 0),
              2)

# Mostrar rectangulo
cv2.rectangle(foto_prueba,
              (lugar_cara_D[3], lugar_cara_D[0]),
              (lugar_cara_D[1],lugar_cara_D[2]),
              (0, 255, 0),
              2)

# Realizar la comparacion
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_D)

# Medida de la distancia
distancia = fr.face_distance([cara_codificada_A], cara_codificada_D)

# Mostrar resultado
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50, 50),  # Posion
            cv2.FONT_HERSHEY_COMPLEX,  # Tipo de letra
            1,  # Escala de la letra
            (0, 255, 0),  # Color
            2)  # grosor

# Mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)


# Mantener programa abierto
cv2.waitKey(0)
