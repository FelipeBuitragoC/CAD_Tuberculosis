import numpy as np


def validate_image(decoded_img: np.ndarray, image_format: str, metrics: dict[str, float], threshold_metrics: dict[str, float]) -> tuple[bool, list[str]]:
    """
    Valida características técnicas y métricas de calidad
    de una imagen.

    Args:
        decoded_img:
            Imagen decodificada.

        image_format:
            Formato de la imagen.

        metrics:
            Métricas calculadas previamente.

        threshold_metrics:
            Umbrales definidos para aceptar/rechazar.

    Returns:
        (valid, issues)
    """

    issues = []

    # Validaciones estructurales

    if not isinstance(decoded_img, np.ndarray):
        issues.append("El tipo de imagen debe ser numpy.ndarray")

    if decoded_img is None or decoded_img.size == 0:
        issues.append("La imagen está vacía")

    if decoded_img.shape != (512, 512):
        issues.append(f"Dimensión inválida: {decoded_img.shape}")

    if image_format not in ["JPG", "PNG", "WEBP"]:
        issues.append(f"Formato no soportado: {image_format}")

    # Validación de métricas

    for metric, value in metrics.items():

        if metric not in threshold_metrics:
            continue

        threshold = threshold_metrics[metric]

        if "min" in threshold and value < threshold["min"]:
            issues.append(
                f"{metric} está por debajo del mínimo permitido"
            )

        if "max" in threshold and value > threshold["max"]:
            issues.append(
                f"{metric} supera el máximo permitido"
            )

    return len(issues) == 0, issues