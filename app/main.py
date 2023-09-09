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

    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario de Python
        data = response.json()

        # Filtra los atributos que deseas utilizar
        filtered_data = {
            "temp_c": data["current"]["temp_c"],
            "precip_mm": data["current"]["precip_mm"],
            # Agrega aquí más atributos que desees
        }
        print(filtered_data)

        # Devuelve los datos filtrados como respuesta
        #return JSONResponse(content=filtered_data)
        return filtered_data
    else:
        # Maneja los casos en los que la solicitud no fue exitosa
        return {"error": "Error en la solicitud"}
    
    #return JSONResponse(content=filtered_data)




