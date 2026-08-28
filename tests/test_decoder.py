from pathlib import Path
from app.image_processing.decoder import decode_image

def test_decode_image():

    """
    Prueba la función decode_image() para decodificar una imagen a partir de sus bytes y determinar su formato.
    """

    image_path = Path("tests/samples/Tuberculosis-121.png")

    image_bytes = image_path.read_bytes()

    decoded_img, image_format = decode_image(image_bytes)   

    print(type(image_bytes))
    print(decoded_img.shape)
    print(image_format)
    print(type(decoded_img))

    assert decoded_img is not None
    assert decoded_img.shape[0] > 0 and decoded_img.shape[1] > 0
    assert image_format == "PNG" or 'PNG' or 'WEBP'