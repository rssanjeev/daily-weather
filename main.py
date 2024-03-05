import time, requests, pandas as pd

def get_data():
    current_weather_url, weather_code_url = get_url()
    response = requests.get(current_weather_url)
    response2 = requests.get(weather_code_url)
    return pd.DataFrame(response.json()), pd.DataFrame(response2.json())

def get_url():
    current_weather_url = "https://api.open-meteo.com/v1/forecast?latitude=40.7143&longitude=-74.006&current_weather=true&timezone=America%2FNew_York"
    weather_code_url = "https://api.open-meteo.com/v1/forecast?latitude=40.7143&longitude=-74.006&daily=weathercode"
    return current_weather_url, weather_code_url

def process_data():
    current_weather_data, weather_code_data = get_data()
    #data = data.drop(['latitude', 'longitude', 'generationtime_ms', 'utc_offset_seconds','timezone', 'timezone_abbreviation', 'elevation', 'hourly_units'], axis=1)
    #data = data.pivot(columns='hourly')
    print(current_weather_data)
    print(weather_code_data)
    current_weather_data.to_csv('Current.csv')
    weather_code_data.to_csv('WeatherCode`.csv')

def send_data():
    pass

def main():
    pass

if __name__ == '__main__':
    process_data()