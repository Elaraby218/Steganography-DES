import sys
import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Add the directory containing file1.py to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from steganography.des_decryption import extract_and_decrypt_stego_image as start_decrypt
routerDecrypt = APIRouter()

stego_image_path = r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\stegoPhoto.png"
gray_image_path = r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\GrayPhoto.png"
output_gray_image_path = r"H:\subjects\Fth\First Term\secuirty\Project\front\src\Photos\RecoveredGrayPhoto.png"


@routerDecrypt.post("/api/decrypt")
def sayHello():
    res = start_decrypt(stego_image_path, gray_image_path, output_gray_image_path)
    if res == "Success":
        return JSONResponse(content={"message": "Encryption started"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Encryption Faied"}, status_code=400)
