# App for the kitchen images classification

from fastapi import FastAPI
from pydantic import BaseModel
from train import predict_single

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

app = FastAPI()

class ImageDetails(BaseModel):
    image : str

    class Config:
        schema_extra = {
            "example": {
                "image": "https://xcdn.next.co.uk/common/Items/Default/Default/Publications/G85/shotview-315x472/8164/M05-222s.jpg"
            }
        }

@app.on_event("startup")
async def startup_event():
    from tensorflow import keras
    global model
    logging.info("Starting stream...")
    logging.info("Loading model...")
    model = keras.models.load_model('./kitchen-images/models/model_kaggle.h')


@app.get("/")
async def root():
    return {"message": "ML Project for Kitchen images classification"}

@app.post("/predict")
async def predict(image: ImageDetails):
    logging.info(f"Predicting image: {image.image}")
    return predict_single(model, image.image, web=True)



