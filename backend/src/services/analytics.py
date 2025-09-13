from typing import Any, Dict
from PIL import Image
import numpy as np

def process_image(image: Image.Image) -> Dict[str, Any]:
    
    image_array = np.array(image)

    
    results = {
        "mean_color": image_array.mean(axis=(0, 1)).tolist(),
        "shape": image_array.shape,
        "size": image_array.size
    }

    return results

def analyze_photo(image: Image.Image) -> Dict[str, Any]:
    analytics_results = process_image(image)

    return analytics_results