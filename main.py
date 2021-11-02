from fastapi import FastAPI, File, UploadFile
import uvicorn
from utilities import *


app = FastAPI()

@app.get("/")
def get_status():
    return {"status": "API is live & working!"}

@app.get("/info")
def get_info():
    return {"endpoints": "Available endpoints are :",
            "/register": "to add a relative",
            "/recognize": "to search relative "}

@app.post("/recognize")
async def get_relative(file:UploadFile= File(...)):
    # verifying uploaded file is an image
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return {"status": "Image must be jpg or png format!"}

    # converting image to desired format
    image = read_imagefile(await file.read())
    # search from available encodings
    status = searchRelative(image)
    return status



@app.post("/register")
async def add_relative(name: str, file:UploadFile= File(...)):
    # verifying uploaded file is an image
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return {"status" : "Image must be jpg or png format!"}

    # converting image to desired format
    image = read_imagefile(await file.read())
    # generate encoding and add relative
    status = registerRelative(name, image)
    return status

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='localhost')