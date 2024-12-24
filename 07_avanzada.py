from PIL import Image, ImageEnhance, ImageFilter, ImageChops

# Brillo 

imagen_original = Image.open('pillow.png')
brillo = ImageEnhance.Brightness(imagen_original)
imagen_cambiada = brillo.enhance(2.0)
imagen_cambiada.save('pillow_brillo.png')
#imagen_cambiada.show()

#Filtro desenfoque 

imagen_desenfocada = imagen_original.filter(ImageFilter.BLUR)
imagen_desenfocada.save('pillow_desenfocada.png')
#imagen_desenfocada.show()

# traduccion: mover imagen

def traduccion(ruta_imagen, desp_x, desp_y ):
    imagen = Image.open(ruta_imagen)
    imagen_traducida = ImageChops.offset(imagen, desp_x, desp_y)
    imagen_traducida.save('imagen_traducida.png')
traduccion('pillow.png', 100, 100)


# Escalado

def escalar_imagen(ruta_imagen, escala) :
    imagen = Image.open(ruta_imagen)
    #print(imagen.size)
    ancho_nuevo = int(imagen.width * escala)
    alto_nuevo = int(imagen.height * escala)
    imagen_escalada = imagen.resize((ancho_nuevo, alto_nuevo))
    imagen_escalada.save('imagen_escalada.png')
    #print(imagen_escalada.size)
escalar_imagen('pillow.png', 3)


#Rotacion
def rotar_imagen(ruta_imagen, angulo) :
    imagen = Image.open(ruta_imagen)
    imagen_rotada = imagen.rotate(angulo)
    imagen_rotada.save('imagen_rotada.png')
rotar_imagen('pillow.png', 45)


