import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import cleaned_data_file

def plot_weather_trends():
    """Visualize temperature and humidity trends over time"""
    df = pd.read_csv(cleaned_data_file)
    df["date"] = pd.to_datetime(df["date"])
    
    # Temperature trends
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=df["date"], y=df["temp_day"], label="Day Temperature", marker="o")
    sns.lineplot(x=df["date"], y=df["temp_night"], label="Night Temperature", marker="s")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trends Over Time")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()
    
    # Humidity trends
    plt.figure(figsize=(10, 5))
    sns.barplot(x=df["date"], y=df["humidity"], color="blue")
    plt.xlabel("Date")
    plt.ylabel("Humidity (%)")
    plt.title("Humidity Levels Over Time")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    plot_weather_trends()
