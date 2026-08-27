import filetype
import numpy as np
import cv2

def decode_image(image_byte: bytes) -> tuple[np.ndarray, str]:

    """
    Decodifica una imagen a partir de sus bytes y determina su formato.

    Returns:
        tuple[np.ndarray, str]: Una tupla con la imagen decodificada y su formato
    """

    image_format: str = None

    # np.frombuffer convierte los bytes en un array de numpy
    # cv2.imdecode decodifica el array de bytes en una imagen en escala de grises
    arr_bytes: np.ndarray = np.frombuffer(image_byte, dtype=np.uint8)
    image: np.ndarray = cv2.imdecode(arr_bytes, cv2.IMREAD_GRAYSCALE)

    # filetype.guess determina el tipo de archivo a partir de los bytes
    kind: filetype.FileType = filetype.guess(image_byte)

    if image is not None:
        print("Imagen decodificada correctamente", image.shape)
    else:
        raise ValueError("No se pudo decodificar la imagen. Formato inválido o corrupto.")

    if kind is not None:
        #image_format = kind.extension.upper() # Retorna 'JPG', 'PNG', 'WEBP', etc....
        image_format = kind.extension.upper()
    else:
        raise ValueError("No se pudo determinar el formato de la imagen. Formato inválido o corrupto.")

    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # redimensionar imagen a 512x512 si no tiene esas dimensiones
    if image.shape != (512, 512):
        image = cv2.resize(image, (512, 512), interpolation=cv2.INTER_AREA)
    
    return (image, image_format)