# Weather Trends and Predictions

## Overview
Fetches weather data using the OpenWeather One Call 3.0 API, processes it, visualizes trends, and applies simple machine learning to predict future temperatures.

## Features
- Fetches real-time and historical weather data
- Processs and cleans raw data
- Visualizes temperature and humidity trends
- Trains a basic machine learning model for temp prediction

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/bnalberti/weather-trends.git
   cd weather-trends
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your OpenWeather API key in `config.py`.

## Usage
Run the scripts in the following order:
1. Fetch weather data:
   ```sh
   python src/fetch_weather.py
   ```
2. Process data:
   ```sh
   python src/process_data.py
   ```
3. Visualize trends:
   ```sh
   python src/visualize_data.py
   ```
4. Train model:
   ```sh
   python src/predict_weather.py
   ```

## Dependencies
- Python 3.8+
- Requests
- Pandas
- Matplotlib & Seaborn
- Scikit-learn

## License
This project is open-source under the MIT License.