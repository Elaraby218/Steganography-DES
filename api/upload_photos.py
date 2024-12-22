from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import shutil

router = APIRouter()

photos_dir_gray = Path("H:/subjects/Fth/First Term/secuirty/Project/front/src/Photos")
photos_dir_gray.mkdir(parents=True, exist_ok=True)

@router.post("/api/upload/Gray")
async def upload_gray_image(file: UploadFile = File(...)):
    print("Uploading Gray image")
    try:
        file_path = photos_dir_gray / f"GrayPhoto{Path(file.filename).suffix}"

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return JSONResponse(content={"message": "Gray image uploaded successfully"}, status_code=200)

    except Exception as e:
        print(f"Error during Gray image upload: {e}")
        raise HTTPException(status_code=500, detail="Error uploading Gray image")


photos_dir_rgb = Path("H:/subjects/Fth/First Term/secuirty/Project/front/src/Photos")
photos_dir_rgb.mkdir(parents=True, exist_ok=True)

@router.post("/api/upload/RGB")
async def upload_rgb_image(file: UploadFile = File(...)):
    print("Uploading RGB image")
    try:
        file_path = photos_dir_rgb / f"RGBPhoto{Path(file.filename).suffix}"

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return JSONResponse(content={"message": "RGB image uploaded successfully"}, status_code=200)

    except Exception as e:
        print(f"Error during RGB image upload: {e}")
        raise HTTPException(status_code=500, detail="Error uploading RGB image")

@router.post("/api/upload/stego")
async def upload_stego_image(file: UploadFile = File(...)):
    print("Uploading stego image")
    try:
        file_path = photos_dir_rgb / f"stegoPhoto{Path(file.filename).suffix}"

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return JSONResponse(content={"message": "stego image uploaded successfully"}, status_code=200)

    except Exception as e:
        print(f"Error during stego image upload: {e}")
        raise HTTPException(status_code=500, detail="Error uploading RGB image")