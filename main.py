from pydantic import BaseModel
from fastapi import FastAPI
from mangum import Mangum
import pickle
import os


class Passenger(BaseModel):
    pclass: int
    sex: int
    age: int
    fare: int
    embarked: int
    title: int
    is_alone: int
    age_class: int


stage = os.environ.get('STAGE', None)
open_api_prefix = f"/{stage}" if stage else "/"
app = FastAPI(title="TitanicAPI", openapi_prefix=open_api_prefix)

with open("random_forest.pkl", "rb") as file:
    model = pickle.load(file)


@app.get('/')
def read_root():
    return {'message': "This is the API's home page"}


# try using async here for lower latency with multiple predictions
@app.post("/passengers")
def model_prediction(data: Passenger):
    received = data.dict()
    pclass = received['pclass']
    sex = received['sex']
    age = received['age']
    fare = received['fare']
    embarked = received['embarked']
    title = received['title']
    is_alone = received['is_alone']
    age_class = received['age_class']

    features = [pclass, sex, age, fare, embarked, title, is_alone, age_class]

    prediction = model.predict([features]).tolist()[0]
    return {'prediction': prediction}


handler = Mangum(app)