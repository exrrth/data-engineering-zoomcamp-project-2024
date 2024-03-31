import os
from etls.air_pollution_etl import extract_air_quality_data, extract_location_data, transform_data, load_data_to_csv
from airflow.models import XCom
from datetime import datetime, timedelta
import pandas as pd

def air_quality_pipeline(locations, **kwargs):
    all_transformed_data = []
    for location in locations:
        latitude = location['latitude']
        longitude = location['longitude']
        
        # Get location name 
        city, country = extract_location_data(latitude, longitude)

        # Get air quality data
        air_quality_data = extract_air_quality_data(latitude, longitude)

        # Transform the data
        transformed_data = transform_data(air_quality_data, city, country)
        
        all_transformed_data.append(transformed_data)

    # Combine data for all locations
    combined_data = pd.concat(all_transformed_data)

    output_directory = os.path.join("data", "output")

    # Load to CSV
    load_data_to_csv(combined_data, output_directory, "combined", "data")

    current_time_utc = datetime.utcnow()
    current_time_gmt7 = current_time_utc + timedelta(hours=7)
    current_time_gmt7_str = current_time_gmt7.strftime("%Y_%m_%d-%H_%M_%S")

    # Push file path to XCom
    file_path = os.path.join(output_directory, f"Air_Quality_Data_{current_time_gmt7_str}.csv")
    kwargs['ti'].xcom_push(key='file_path', value=file_path)
