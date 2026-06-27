import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator
from fastapi.responses import JSONResponse
from typing import Annotated

# Load the model
with open("model.pkl", 'rb') as f:

    model = pickle.load(f)

app = FastAPI()

class Student(BaseModel):
    Hours_of_Study: Annotated[float, Field(description='Hours_of_Study', examples=[2.5])]
    Hours_of_Playing: Annotated[float, Field(description='Hours_of_Playing', examples=[2.5])]

    @field_validator('Hours_of_Study', 'Hours_of_Playing')
    @classmethod
    def validate_hours(cls, value: float) -> float:
        if 0 <= value <= 12:
            return value
        else:
            raise ValueError("Hours must be between 0 and 12")

@app.get('/')
def home():
    return JSONResponse(status_code=202, content={'message': 'API connected'})

@app.post('/predict')
def prediction(inputdata: Student):
    datainfo = pd.DataFrame([{
        'Hours_of_Study': inputdata.Hours_of_Study,
        'Hours_of_Playing': inputdata.Hours_of_Playing
    }])
    
    predict_result = float(model.predict(datainfo)[0])
    return JSONResponse(status_code=200, content={'prediction': predict_result,'Result':"Pass" if predict_result == 1 else "Fail"})