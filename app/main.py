from fastapi import FastAPI
from dotenv import load_dotenv
from .events import Emit
import os
import requests
import pika
import logging

emit_events = Emit()

url = "https://weatherapi-com.p.rapidapi.com/current.json"
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

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

    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario de Python
        data = response.json()

        # Filtra los atributos que deseas utilizar
        filtered_data = {
            "temp_c": data["current"]["temp_c"],
            "precip_mm": data["current"]["precip_mm"],
            # Agrega aquí más atributos que desees
        }
        logging.info(f"El clima en {querystring['q']} es de {filtered_data['temp_c']}°C")
        emit_events.send(1, "check", filtered_data)
        # Devuelve los datos filtrados como respuesta
        #return JSONResponse(content=filtered_data)
        return filtered_data
    else:
        # Maneja los casos en los que la solicitud no fue exitosa
        return {"error": "Error en la solicitud"}
    
    #return JSONResponse(content=filtered_data)
