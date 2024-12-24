from PIL import Image
imagen = Image.open('pillow.png')
imagen.transpose(Image.FLIP_LEFT_RIGHT).save('pillow_volteada.png')
imagen.rotate(90).save('pillow_rotada.png')
imagen.crop((200,50,450,300)).save('pillow_recortada.png')

imagen_grises = imagen.convert('L')
imagen_grises.save('pillow_grises.png')

#filtro

from PIL import ImageFilter
imagen_filtrada = imagen.filter(ImageFilter.BLUR)
imagen_filtrada.save('pillow_filtrada.png')