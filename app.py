from fastapi import FastAPI
from pydantic import BaseModel,Field,computed_field,field_validator
from fastapi.responses import JSONResponse
from schema.prediction_response import PredictionResponse
from typing import Literal,Annotated
from schema.user_input import UserInput
from config.city_tier import tier_1_cities,tier_2_cities
from model.predict import predict_output


app=FastAPI()

tier_1_cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Ahmedabad']

tier_2_cities = ['Jaipur', 'Lucknow', 'Kanpur', 'Nagpur', 'Indore', 'Bhopal', 'Coimbatore', 'Kochi', 'Visakhapatnam', 'Vadodara', 'Surat', 'Chandigarh', 'Patna', 'Madurai', 'Nashik', 'Vijayawada', 'Mysuru', 'Thiruvananthapuram', 'Rajkot', 'Guwahati']

    
@app.get('/')
def home():
    return {"message":"this is the insurance premium category prediction api"}

@app.get('/health')
def health_chech():
    return {
        'status':"ok"
    }
    
@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data:UserInput):
    user_input={
        "bmi":data.bmi,
        "income_lpa":data.income_lpa,
        "occupation":data.occupation,
        "age_group":data.age_group,
        "lifestyle_risk":data.lifestyle_risk,
        "city_tier":data.city_tier,

    }
    try:
        prediction=predict_output(user_input)
        return JSONResponse(status_code=200,content={"predicted_category":prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))










