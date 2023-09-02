import time, requests, pandas as pd

def get_data():
    url = f"https://api.open-meteo.com/v1/forecast?latitude=40.3428&longitude=-105.6836&hourly=temperature_2m,precipitation_probability,rain,snowfall,cloudcover,cloudcover_low,cloudcover_mid,cloudcover_high,visibility&timezone=America%2FDenver"
    response = requests.get(url)
    return pd.DataFrame(response.json())

def process_data():
    data = get_data()
    data = data.drop(['latitude', 'longitude', 'generationtime_ms', 'utc_offset_seconds','timezone', 'timezone_abbreviation', 'elevation', 'hourly_units'], axis=1)
    data = data.pivot(columns='hourly')
    print(data.columns)
    data.to_csv('Hourly.csv')

def send_data():
    pass

def main():
    pass

if __name__ == '__main__':
    process_data()