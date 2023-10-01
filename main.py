import time, requests, pandas as pd

def get_data():
    url = "https://api.open-meteo.com/v1/forecast?latitude=40.7143&longitude=-74.006&daily=weathercode,temperature_2m_max,temperature_2m_min,rain_sum&timezone=America%2FDenver"
    response = requests.get(url)
    return pd.DataFrame(response.json())

def process_data():
    data = get_data()
    #data = data.drop(['latitude', 'longitude', 'generationtime_ms', 'utc_offset_seconds','timezone', 'timezone_abbreviation', 'elevation', 'hourly_units'], axis=1)
    #data = data.pivot(columns='hourly')
    print(data)
    #data.to_csv('Hourly.csv')

def send_data():
    pass

def main():
    pass

if __name__ == '__main__':
    process_data()