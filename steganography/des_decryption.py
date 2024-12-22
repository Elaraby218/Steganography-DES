
from PIL import Image
from .des_encrypt import decryption

from PIL import Image

def extract_and_decrypt_stego_image(stego_image_path, gray_image_path, output_gray_image_path):
    try:
        print("start decrypting")
        # Step 1: Load the gray image to get dimensions
        gray_image = Image.open(gray_image_path)
        width, height = gray_image.size
        total_pixels = width * height

        # Step 2: Load the stego image and convert it to bytes
        stego_image = Image.open(stego_image_path)
        stego_data = list(stego_image.tobytes())

        # Step 3: Extract the last bit of each byte from the stego data
        extracted_bits = [byte & 1 for byte in stego_data]

        # Step 4: Group every 8 bits into integers
        extracted_integers = [
            int(''.join(map(str, extracted_bits[i:i+8])), 2)
            for i in range(0, len(extracted_bits), 8)
        ]

        # Step 5: Decrypt the extracted data 8 bytes (8 integers) at a time
        decrypted_data = []
        for i in range(0, len(extracted_integers), 8):
            chunk = extracted_integers[i:i+8]

            # Ensure the chunk is exactly 8 bytes (pad with zeros if necessary)
            if len(chunk) < 8:
                chunk += [0] * (8 - len(chunk))

            # Call the decryption function for the current chunk
            decrypted_chunk = decryption(chunk)
            decrypted_data.extend(decrypted_chunk)

        # print("decrytped data here :  " , decrypted_data)
        # Step 6: Reconstruct the grayscale image
        gray_image_data = bytes(decrypted_data[:total_pixels])  # Ensure it fits the original size
        reconstructed_image = Image.frombytes("L", (width, height), gray_image_data)

        # Step 7: Save the grayscale image to the specified path
        reconstructed_image.save(output_gray_image_path)
        print(f"Reconstructed grayscale image saved at: {output_gray_image_path}")
        return "Success"
    except Exception as e:
        print(f"Error processing image: {e}")
        return "Error"

# Define file paths
stego_image_path = r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\stegoPhoto.png"
gray_image_path = r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\GrayPhoto.png"
output_gray_image_path = r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\RecoveredGrayPhoto.png"


# Call the function
# extract_and_decrypt_stego_image(stego_image_path, gray_image_path, output_gray_image_path)

