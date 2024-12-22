from PIL import Image
from .des_encrypt import decryption


def extract_and_decrypt_stego_image(stego_image_path, output_gray_image_path):
    try:
        print("start decrypting")


        stego_image = Image.open(stego_image_path)
        stego_data = list(stego_image.tobytes())


        width_bits = [byte & 1 for byte in stego_data[:32]]
        width = int(''.join(map(str, width_bits)), 2)
        print(f"Extracted width of gray image: {width} pixels")

        height_bits = [byte & 1 for byte in stego_data[32:64]]
        height = int(''.join(map(str, height_bits)), 2)
        print(f"Extracted height of gray image: {height} pixels")


        extracted_bits = [byte & 1 for byte in stego_data[64:]]


        extracted_integers = [
            int(''.join(map(str, extracted_bits[i:i + 8])), 2)
            for i in range(0, len(extracted_bits), 8)
        ]

        decrypted_data = []
        for i in range(0, len(extracted_integers), 8):
            chunk = extracted_integers[i:i + 8]

            if len(chunk) < 8:
                chunk += [0] * (8 - len(chunk))

            decrypted_chunk = decryption(chunk)
            decrypted_data.extend(decrypted_chunk)


        gray_image_data = bytes(decrypted_data[:width * height])

        reconstructed_image = Image.frombytes("L", (width, height), gray_image_data)

        reconstructed_image.save(output_gray_image_path)
        print(f"Reconstructed grayscale image saved at: {output_gray_image_path}")
        return "Success"

    except Exception as e:
        print(f"Error processing image: {e}")
        return "Error"


# Example usage
stego_image_path = r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\stegoPhoto.png"
output_gray_image_path = r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\RecoveredGrayPhoto.png"

# extract_and_decrypt_stego_image(stego_image_path, output_gray_image_path)

# Call the function
# extract_and_decrypt_stego_image(stego_image_path, output_gray_image_path)