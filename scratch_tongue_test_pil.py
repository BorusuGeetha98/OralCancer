import numpy as np
from PIL import Image

def is_tongue_pillow(image_content):
    try:
        from io import BytesIO
        img = Image.open(BytesIO(image_content)).convert('RGB')
        # Resize to make processing faster
        img = img.resize((100, 100))
        img_array = np.array(img)
        
        # R, G, B channels
        R = img_array[:, :, 0]
        G = img_array[:, :, 1]
        B = img_array[:, :, 2]
        
        # Heuristic for red/pink-ish tone (tongue/mouth)
        # Tongue is typically: R > G and R > B. And R is somewhat high.
        # Let's say R > 80, and R > G + 15, and R > B + 15
        red_mask = (R > 80) & (R > G + 15) & (R > B + 15)
        
        red_percentage = np.sum(red_mask) / (100 * 100) * 100
        print(f"Red/Pink pixel percentage: {red_percentage:.2f}%")
        
        # If at least 10% of the image is strongly pink/red, assume it might be a tongue/mouth
        return red_percentage > 5.0
    except Exception as e:
        print(f"Error checking image: {e}")
        return True # Default to true so we don't break prediction
