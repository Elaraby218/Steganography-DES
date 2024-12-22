from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.upload_photos import router as uploadPhotos
from api.encrypt_photo import routerEncrypt as encrypt_router
from api.decrypt_photo import routerDecrypt as decrypt_router

app = FastAPI()

origins = ["http://localhost:3000"]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(uploadPhotos)
app.include_router(encrypt_router)
app.include_router(decrypt_router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the API"}


