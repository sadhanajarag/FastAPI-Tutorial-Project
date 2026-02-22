from fastapi import FastAPI
from pydantic import BaseModel
from model import model
import numpy as np

app = FastAPI()


class IrisFlower(BaseModel):
    SepalLengthCm : float
    SepalWidthCm:float
    PetalLengthCm : float
    PetalWidthCm : float


@app.post('/predict')
def predict(data : IrisFlower):
    feature = np.array([
        [
            data.SepalLengthCm,
            data.SepalWidthCm,
            data.PetalLengthCm,
            data.PetalWidthCm
        ]
    ])

    prediction = model.predict(feature)
    return {'prediction': int(prediction[0])}