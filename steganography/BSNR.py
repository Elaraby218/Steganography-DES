from PIL import Image
import numpy as np

def calculate_bsnr(original_image_path, encrypted_image_path):
    # Load the original and encrypted images in grayscale mode
    original_image = Image.open(original_image_path).convert('L')
    encrypted_image = Image.open(encrypted_image_path).convert('L')

    # Convert images to NumPy arrays
    original_pixels = np.array(original_image, dtype=np.float64)
    encrypted_pixels = np.array(encrypted_image, dtype=np.float64)

    # Calculate the mean of the original image
    mean_original = np.mean(original_pixels)

    # Calculate the signal energy
    signal_energy = np.sum((original_pixels - mean_original) ** 2)

    # Calculate the noise energy
    noise_energy = np.sum((encrypted_pixels - original_pixels) ** 2)

    # Avoid division by zero
    if noise_energy == 0:
        return float('inf')

    # Calculate BSNR
    bsnr = 10 * np.log10(signal_energy / noise_energy)
    return bsnr

# Paths to images
original_image_path = r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\RGBPhoto.png"
encrypted_image_path= r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\stegoPhoto.png"

# Calculate BSNR
bsnr_value = calculate_bsnr(original_image_path, encrypted_image_path)
print(f"BSNR Value: {bsnr_value:.2f} dB")
