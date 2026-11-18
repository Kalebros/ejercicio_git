from loguru import logger
import os

CURRENT_DIR = os.path.dirname(__file__)

logger.info('Hola mundo!')

contenido = os.listdir(CURRENT_DIR)
logger.info(f'Contenido del directorio: {contenido}')

informacion_archivos = []
for archivo in contenido:
    if archivo.endswith('.txt'):
        with open(archivo, "r", encoding="utf-8") as archivo:
            nombre_actual = archivo.read()
            if nombre_actual.strip() == "":
                logger.warning(f'El archivo {archivo.name} está vacío')
            else:
                logger.info(f'Contenido del archivo: {nombre_actual}')
            informacion_archivos.append(nombre_actual.strip())

with open('nombres_completos.txt', 'w', encoding='utf-8') as archivo_salida:
    for nombre in informacion_archivos:
        archivo_salida.write(nombre+'\n')
