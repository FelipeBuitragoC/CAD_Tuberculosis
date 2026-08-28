from pathlib import Path
from app.image_processing.quality import calculate_metrics

def test_calculate_metrics():
    """
    Prueba la función calculate_metrics() para calcular métricas de calidad de imagen.
    """

    image_path = Path("tests/samples/Tuberculosis-121.png")

    image_bytes = image_path.read_bytes()

    # Decodificar la imagen a partir de sus bytes
    from app.image_processing.decoder import decode_image
    decoded_img, image_format = decode_image(image_bytes)

    metrics = calculate_metrics(decoded_img)

    print(metrics)

    assert isinstance(metrics, dict)
    assert "brightness" in metrics
    assert "contrast" in metrics
    assert "entropy" in metrics
    assert "dynamic_range" in metrics
    assert "blur_score" in metrics
    assert "underexposed_ratio" in metrics
    assert "overexposed_ratio" in metrics
    assert "noise_estimate" in metrics