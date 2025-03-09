api_key = '83784515145bbdd280ee551f98bf23da '
main_url = "https://api.openweathermap.org/data/3.0/onecall"
default_location = {"lat": 51.5072, "lon": -0.1276}  # London

headers = {
	"Content-Type": "application/json"
}

# Filepaths
data_folder = "data/"
raw_data_file = data_folder + "weather_data.json"
cleaned_data_file = data_folder + "weather_data.csv"
