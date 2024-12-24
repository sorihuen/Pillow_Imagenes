from PIL import Image
imagen = Image.open('pillow.png')
imagen = imagen.convert('RGB')
imagen.save('pillow_cambiada.jpg')
imagen.thumbnail((200,200))
imagen.save('pillow_miniatura.jpg')