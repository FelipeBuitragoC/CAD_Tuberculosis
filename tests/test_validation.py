from pathlib import Path

from app.image_processing.decoder import decode_image
from app.image_processing.quality import calculate_metrics
from app.image_processing.validation import validate_image


def test_validate_image():
    """
    Prueba la función validate_image().
    """

    image_path = Path("tests/samples/Tuberculosis-121.png")

    image_bytes = image_path.read_bytes()

    # Decodificar imagen
    decoded_img, image_format = decode_image(image_bytes)

    # Calcular metricas
    metrics = calculate_metrics(decoded_img)

    threshold_metrics = {
        "brightness": {
            "min": 30,
            "max": 220
        },
        "contrast": {
            "min": 20
        },
        "entropy": {
            "min": 4
        },
        "dynamic_range": {
            "min": 50
        },
        "blur_score": {
            "min": 100
        },
        "underexposed_ratio": {
            "max": 0.15
        },
        "overexposed_ratio": {
            "max": 0.10
        },
        "noise_estimate": {
            "max": 15
        }
    }

    is_valid, issues = validate_image(
        decoded_img,
        image_format,
        metrics,
        threshold_metrics
    )

    print("Metrics:")
    print(metrics)

    print(f"Is valid: {is_valid}")
    print(f"Issues: {issues}")

    assert isinstance(is_valid, bool)
    assert isinstance(issues, list)