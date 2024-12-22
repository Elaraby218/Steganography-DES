import sys
import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Add the directory containing file1.py to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from steganography.des_encrypt import start_encrypt
routerEncrypt = APIRouter()



@routerEncrypt.post("/api/encrypt")
def sayHello():
    res = start_encrypt()
    if res == "Success":
        return JSONResponse(content={"message": "Encryption started"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Encryption Faied"}, status_code=400)
