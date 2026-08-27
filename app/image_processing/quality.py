import numpy as np
import skimage.measure
from scipy.stats import iqr
import cv2
from skimage.restoration import estimate_sigma

def calculate_metrics(image: np.ndarray, threshold_black: float = 5, threshold_white: float = 250) -> dict[str, float]:
    """
    Calcula metricas
    Args:
        image (np.ndarray): La imagen de entrada
        threshold_black (float): Umbral para considerar un pixel como subexpuesto
        threshold_white (float): Umbral para considerar un pixel como sobreexpuesto

    Returns:
        dict[str, float]: Un diccionario con las metricas calculadas
    """

    brightness = float(np.mean(image))
    contrast = float(np.std(image))
    entropy = float(skimage.measure.shannon_entropy(image))
    dynamic_range = float(iqr(image, rng=(5, 95)))
    blur_score = float(cv2.Laplacian(image, cv2.CV_64F).var())
    underexposed_ratio = float(np.mean(image < threshold_black))
    overexposed_ratio = float(np.mean(image > threshold_white))
    noise_estimate = float(estimate_sigma(image, channel_axis=None, average_sigmas=True))

    return {
        "brightness": brightness,
        "contrast": contrast,
        "entropy": entropy,
        "dynamic_range": dynamic_range,
        "blur_score": blur_score,
        "underexposed_ratio": underexposed_ratio,
        "overexposed_ratio": overexposed_ratio,
        "noise_estimate": noise_estimate
    }