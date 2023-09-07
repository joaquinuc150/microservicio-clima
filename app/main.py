from fastapi import FastAPI
from dotenv import load_dotenv
import os
import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"Santiago"}

load_dotenv()

headers = {
	"X-RapidAPI-Key": os.getenv('RAPID_API_KEY'),
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/weather")
async def weather():
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()