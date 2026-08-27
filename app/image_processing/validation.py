import numpy as np

from app.image_processing.quality import calculate_metrics


def validate_image(decoded_img: np.ndarray, image_format: str, threshold_metrics: dict[str, float]) -> tuple[bool, list]:
    """
    Valida la imagen decodificada y su formato.

    Args:
        decoded_img (np.ndarray): Imagen decodificada.
        image_format (str): Formato de la imagen.

    Returns:
        tuple[bool, list]: Una tupla con un valor booleano que indica si la imagen es válida y una lista de mensajes de error en caso de que no lo sea.
    """
    valid: bool = True
    issue: list[str] = []

    metrics = calculate_metrics(decoded_img)

    if type(decoded_img) is not np.ndarray:
        issue.append("El tipo de la imagen decodificada debe ser un array de numpy.")

    if decoded_img.shape != (512, 512):
        issue.append(f"La imagen decodificada debe tener dimensiones 512x512, pero tiene {decoded_img.shape}.")

    if decoded_img is None or decoded_img.size == 0:
        issue.append("La imagen decodificada es inválida o está vacía.")

    if image_format not in ["JPG", "PNG", "WEBP"]:
        issue.append(f"Formato de imagen no soportado: {image_format}")

    metrics = calculate_metrics(decoded_img)
    
    for metric, value in metrics.items():
        if metric in threshold_metrics:
            if value > threshold_metrics[metric]:
                issue.append(f"La métrica {metric} es mayor que el umbral: {value} > {threshold_metrics[metric]}")

    return len(issue)==0, issue