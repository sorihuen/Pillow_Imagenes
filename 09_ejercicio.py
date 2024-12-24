from PIL import Image, ImageDraw, ImageFont

def aplicar_filtro_sepia(imagen):
    width, height = imagen.size
    pixels = imagen.load() 

    for py in range(height):
        for px in range(width):
            if len(imagen.getpixel((px, py))) == 4:
                r, g, b, a = imagen.getpixel((px, py))
            else:
                r, g, b = imagen.getpixel((px, py))
                a = 255

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                tr = 255
            if tg > 255:
                tg = 255
            if tb > 255:
                tb = 255

            pixels[px, py] = (tr, tg, tb, a)

    return imagen

def agregar_texto(imagen, texto, posicion, tamano_fuente, color_texto):
    draw = ImageDraw.Draw(imagen)
    font = ImageFont.truetype("arial.ttf", tamano_fuente)
    draw.text(posicion, texto, font=font, fill=color_texto)
    return imagen

# Cargar la imagen
imagen = Image.open('pillow.png')

# Aplicar filtro de sepia
imagen_sepia = aplicar_filtro_sepia(imagen)

# Agregar texto
texto = "Si se puede"
posicion = (10, 10)
tamano_fuente = 40
color_texto = (255, 255, 255)

imagen_con_texto = agregar_texto(imagen_sepia, texto, posicion, tamano_fuente, color_texto)

# Convertir a modo RGB antes de guardar como JPEG
imagen_con_texto = imagen_con_texto.convert("RGB")

# Guardar y mostrar la imagen resultante
imagen_con_texto.save('imagen_editada.jpg')
imagen_con_texto.show()


