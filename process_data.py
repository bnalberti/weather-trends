import json
import pandas as pd
from config import raw_data_file, cleaned_data_file

def process_weather_data():
    """Load raw weather data, extract relevant fields, and save as CSV."""
    with open(raw_data_file, "r") as file:
        data = json.load(file)
    
	# Extract relevant data
    daily_data = data.get("daily", [])
    processed_data = []
    
    for day in daily_data:
        processed_data.append({
            "date": pd.to_datetime(day["dt"], unit="s"),
            "temp_day": day["temp"]["day"],
            "temp_night": day["temp"]["night"],
            "humidity": day["humidity"],
            "wind_speed": day["wind_speed"],
            "weather": day["weather"][0]["description"]
        })
    
	# Save to CSV
    df = pd.DataFrame(processed_data)
    df.to_csv(cleaned_data_file, index=False)
    print(f"Processed data saved to {cleaned_data_file}")

if __name__ == "__main__":
	process_weather_data()
