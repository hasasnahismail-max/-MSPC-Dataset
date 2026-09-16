import cv2
import numpy as np
import os

def process_surface_image(image_path, output_path):
    """
    Reads an industrial component image, applies preprocessing (CLAHE, denoising),
    and isolates structural cracks using adaptive thresholding and contour detection.
    """
    # Load image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error loading image: {image_path}")
        return

    # Resize to standard model input dimension
    img_resized = cv2.resize(img, (640, 640))

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to enhance surface cracks
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(img_resized)

    # Gaussian Blur to reduce high-frequency manufacturing texture noise
    blurred = cv2.GaussianBlur(enhanced, (5, 5), 0)

    # Adaptive Thresholding to isolate crack edges
    thresh = cv2.adaptiveThreshold(
        blurred, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 11, 2
    )

    # Morphological operations to clean up isolated noise pixels
    kernel = np.ones((2, 2), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Save processed diagnostic mask
    cv2.imwrite(output_path, cleaned)
    print(f"Processed and saved: {output_path}")

if __name__ == "__main__":
    print("MSPC-Dataset Pipeline Initialized. Ready for batch processing.")
