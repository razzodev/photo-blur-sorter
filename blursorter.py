import cv2
import numpy as np
import os
import argparse
import rawpy

def variance_of_laplacian(image):
    """Computes the Laplacian variance of an image."""
    return np.var(cv2.Laplacian(image, cv2.CV_64F))

def is_blurry(image, threshold=500.0):  # Default threshold bumped to 500
    """Checks if an image (already loaded) is blurry."""
    return variance_of_laplacian(image) < threshold

def load_image(image_path):
    """Loads an image, handling different file types."""
    try:
        if image_path.lower().endswith(('.dng', '.cr2', '.nef', '.arw', '.rw2', '.orf', '.raf')):
            with rawpy.imread(image_path) as raw:
                rgb = raw.postprocess(half_size=True)  # Faster processing
                image = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
        else:
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            print(f"Error loading image: {image_path}")
            return None
        return image
    except rawpy.LibRawError as e:
        print(f"Error loading raw image {image_path}: {e}")
        return None
    except Exception as e:
        print(f"Error loading {image_path}: {e}")
        return None

def sort_blurry_images(directory, threshold=500.0, output_subdir="blurry_images"): # Default threshold bumped to 500
    """Sorts blurry images into a subdirectory."""
    output_dir = os.path.join(directory, output_subdir)
    os.makedirs(output_dir, exist_ok=True)

    image_files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.dng', '.cr2', '.nef', '.arw', '.rw2', '.orf', '.raf'))]
    num_images = len(image_files)

    for i, filename in enumerate(image_files):
        filepath = os.path.join(directory, filename)
        image = load_image(filepath)
        if image is not None:
            variance = variance_of_laplacian(image)
            message = f"Processing {filename} ({i+1}/{num_images}): Variance = {variance:.2f} - "
            if is_blurry(image, threshold):
                message += "BLURRY. Moving to " + output_dir
                try:
                    os.rename(filepath, os.path.join(output_dir, filename))
                except FileExistsError:
                    message += "File already exists in destination."
                except OSError as e:
                    message += f"Error moving: {e}"
            else:
                message += "SHARP."
            print(message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sorts blurry images into a separate folder.")
    parser.add_argument("directory", nargs="?", default=".", help="The directory containing the images (defaults to current directory).") # Modified argument
    parser.add_argument("-t", "--threshold", type=float, default=500.0, help="The blur threshold (default: 500).") # Default threshold bumped to 500
    parser.add_argument("-o", "--output", type=str, default="blurry_images", help="The name of the output subdirectory.")
    args = parser.parse_args()

    sort_blurry_images(args.directory, args.threshold, args.output)
