from app.image_processing.decoder import decode_image
from app.image_processing.quality import calculate_metrics
from app.image_processing.validation import validate_image

class ImageQualityService:

    def __init__(self, threshold_metrics: dict[str, float]):
        self.threshold_metrics = threshold_metrics

    def analyze(self, image_bytes: bytes) -> dict:

        # decodificar
        image, image_format = decode_image(image_bytes)

        # calcular metricas
        metrics = calculate_metrics(image)

        # validar
        valid, issues = validate_image(image, image_format, metrics, self.threshold_metrics)

        # resultado final
        return {
            "valid": valid,
            "issues": issues,
            "format": image_format,
            "metrics": metrics
            }