import requests as req
import json
import os
from config import api_key, main_url, default_location, raw_data_file, headers, data_folder

def fetch_weather_data(lat=default_location["lat"], lon=default_location["lon"], save=True):
    """Fetch weather data from OpenWeather API and save it to a file"""
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric",
        "exclude": "minutely,alerts"
    }
    
    response = req.get(main_url, params=params, headers=headers)
	
    if response.status_code == 200:
        data = response.json()
		
        if save:
            os.makedirs(data_folder, exist_ok=True)
            with open(raw_data_file, "w") as file:
                    json.dump(data, file, indent=4)
				
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == "__main__":
	fetch_weather_data()