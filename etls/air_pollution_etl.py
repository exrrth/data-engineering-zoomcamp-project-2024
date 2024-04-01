import os
import requests
import pandas as pd
from datetime import datetime, timedelta
from utils.constants import aqicn_api_key, google_api_key

def extract_air_quality_data(lat, lon):
    aqicn_url = f"http://api.waqi.info/feed/geo:{lat};{lon}/?token={aqicn_api_key}"
    response = requests.get(aqicn_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching air quality data.")
        return None

def extract_location_data(lat, lon):
    google_geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={google_api_key}"
    response = requests.get(google_geocoding_url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            for result in data['results']:
                for component in result['address_components']:
                    if 'country' in component['types']:
                        country = component['long_name']
                    if 'locality' in component['types']:
                        city = component['long_name']
            return city, country
        else:
            print("Geocoding failed.")
            return None, None
    else:
        print("Error fetching location data.")
        return None, None

def calculate_pm25(aqi):
    breakpoints = {
        (0, 50): (0, 12),
        (51, 100): (12.1, 35.4),
        (101, 150): (35.5, 55.4),
        (151, 200): (55.5, 150.4),
        (201, 300): (150.5, 250.4),
        (301, 500): (250.5, 500.4)
    }
    
    for (low, high), (pm25_low, pm25_high) in breakpoints.items():
        if low <= aqi <= high:
            return pm25_low + ((aqi - low) * (pm25_high - pm25_low) / (high - low))

def transform_data(air_quality_data, city, country):
    if air_quality_data is not None:
        air_quality_info = {
            "aqi": air_quality_data["data"].get("aqi"),
            "last_update": pd.Timestamp(air_quality_data["data"]["time"].get("iso")), 
            "city": city,
            "country": country,
            "latitude": air_quality_data["data"]["city"]["geo"][0],
            "longitude": air_quality_data["data"]["city"]["geo"][1],
            "temperature_c": air_quality_data["data"]["iaqi"].get("t", {}).get("v"),
            "humidity_percent": air_quality_data["data"]["iaqi"].get("h", {}).get("v"),
            "wind_speed_m_s": air_quality_data["data"]["iaqi"].get("w", {}).get("v"),
            "pressure_hpa": air_quality_data["data"]["iaqi"].get("p", {}).get("v")
        }

        aqi_category = None
        aqi_value = air_quality_info["aqi"]
        if aqi_value is not None:
            if aqi_value <= 50:
                aqi_category = "Good"
            elif aqi_value <= 100:
                aqi_category = "Moderate"
            elif aqi_value <= 150:
                aqi_category = "Unhealthy for Sensitive Groups"
            elif aqi_value <= 200:
                aqi_category = "Unhealthy"
            elif aqi_value <= 300:
                aqi_category = "Very Unhealthy"
            else:
                aqi_category = "Hazardous"

        pm25 = calculate_pm25(air_quality_info["aqi"])
        air_quality_info["pm25_concentration_ug_per_m3"] = pm25
        
        air_quality_info["aqi_level"] = aqi_category

        df = pd.DataFrame(air_quality_info, index=[0])
        
        constraints = {
            'aqi': int,                     
            'city': str,                    
            'country': str,                
            'latitude': float,            
            'longitude': float,           
            'temperature_c': float,       
            'humidity_percent': float,    
            'wind_speed_m_s': float,       
            'pressure_hpa': float, 
            'pm25_concentration_ug_per_m3': float,  
            'aqi_level': str                
        }

        for col, dtype in constraints.items():
            df[col] = df[col].astype(dtype)
        
        print(df.dtypes)
        
        return df
    else:
        return None

def load_data_to_csv(data, output_directory, city, country):
    if data is not None:
        current_time_utc = datetime.utcnow()
        current_time_gmt7 = current_time_utc + timedelta(hours=7)
        current_time_gmt7_str = current_time_gmt7.strftime("%Y_%m_%d-%H_%M_%S")

        file_name = f"Air_Quality_Data_{current_time_gmt7_str}.csv"

        os.makedirs(output_directory, exist_ok=True)

        output_file_path = os.path.join(output_directory, file_name)
        
        data.to_csv(output_file_path, index=False)
        print(f"Data saved to '{output_file_path}'")
    else:
        print("No data to save.")


