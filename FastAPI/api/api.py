from fastapi import APIRouter, File, UploadFile
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow import expand_dims
from tensorflow.nn import softmax
from numpy import argmax, array
from database.database import save_prediction_to_database
import io

router = APIRouter()

model_dir = "Model/model.h5"
model = load_model(model_dir)

class_predictions = array([
    "chicken_curry",
    "chicken_wings",
    "fried_rice",
    "grilled_salmon",
    "hamburger",
    "ice_cream",
    "pizza",
    "ramen",
    "steak",
    "sushi"
])

@router.post("/net/image/prediction/")
async def get_net_image_prediction(file: UploadFile = File(...)):

    content = await file.read()

    img_stream = io.BytesIO(content)

    img_array = load_and_preprocess_image(img_stream)

    pred = model.predict(img_array)
    score = softmax(pred[0])

    class_prediction = class_predictions[argmax(score)]

    save_prediction_to_database(content, class_prediction)

    return {
        "model-prediction": class_prediction
    }

def load_and_preprocess_image(img_stream):
    img = load_img(img_stream, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = expand_dims(img_array, 0)
    return img_array
