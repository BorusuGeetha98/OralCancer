import cv2
import numpy as np

def is_tongue(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return False
    
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define ranges for red/pinkish color
    # Red in HSV wraps around 0 and 180
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([15, 255, 255])
    
    lower_red2 = np.array([160, 50, 50])
    upper_red2 = np.array([180, 255, 255])
    
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    mask = mask1 + mask2
    
    # Calculate percentage of red/pink pixels
    red_pixels = cv2.countNonZero(mask)
    total_pixels = img.shape[0] * img.shape[1]
    
    red_percentage = (red_pixels / total_pixels) * 100
    print(f"Red/Pink pixel percentage: {red_percentage:.2f}%")
    
    # If more than, say, 5% is red/pink, we consider it valid. (Tongues are very prominent)
    return red_percentage > 5.0

if __name__ == '__main__':
    # You can pass an image path to test
    import sys
    if len(sys.argv) > 1:
        print(is_tongue(sys.argv[1]))
