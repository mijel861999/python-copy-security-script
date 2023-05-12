import shutil
import os


ruta_origen = "C:/Users/Usuario/workspace"
ruta_destino = "E:/copia/workspace"

def realizar_copia():
    # obtener un array con los archivos de la ruta de origen
    elementos = os.listdir(ruta_origen)

    # Recorre la lista y copia cada elemento en la ruta de destino
    for elemento in elementos:
        #Esto crea las nuevas rutas
        origen = os.path.join(ruta_origen, elemento)
        destino = os.path.join(ruta_destino, elemento)


        # Esto verifica si es un directorio o un archivo para utilizar una
        # función de copia adecuada
        if os.path.isdir(origen):
            shutil.copytree(origen, destino)
        else:
            shutil.copy2(origen, destino)
    print("Copia de seguridad")

realizar_copia()
