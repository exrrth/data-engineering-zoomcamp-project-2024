# AIR Quality Data Project

### Problem Statement
The project aim to build end-to-end data pipeline that extract air quality data from api. The extracted data will be processed and enri

### Pipeline Execution (DAG)
- The DAG updates every 20 minutes to ensure data remains up-to-date. Normally, data is scheduled to be updated hourly, but occasional delays occur.

### Data Schema

| Column | Type | 
|--------|-------------|
| aqi | int |
| city | str |
| country | str |
| latitude | float |
| longitude | float |
| temperature_c | float |
| humidity_percent | float |
| wind_speed_m_s | float |
| pressure_hpa | float |
| pm25_concentration_ug_per_m3 | float |
| aqi_level | str |

### Data Pipeline

- **Pipeline**

![image](https://github.com/EarthSuppawoot/air-quality/assets/157554832/b7dd2662-9059-4798-95d7-75d083a85c66)

- **DAG**

![image](https://github.com/EarthSuppawoot/air-quality/assets/157554832/9e79aeb0-e7b6-4101-b711-ae52e9294cdd)

### Technologies and Tools
- **Cloud**: Amazon Web Services (AWS)
- **Containerization**: Docker
- ***Workflow Orchestration**: Apache Airflow
- **Data Lake**: AWS S3
- **Data Warehousing**: Amazon Redshift
- **Data Visualization**: Power BI
- **Language**: Python


### Analytics Dashboard
The dashboard will have four parts with control filter on time and city that represent the analytics points below:

1. **AQI Time Series Plot**: Shows how air quality changes over time.
2. **AQI Visualization Map**: Displays air quality levels in different cities.
3. **Temperature-AQI Relationship Plot**: Explains how temperature affects air quality.
4. **Distribution by AQI Level**: Illustrates how often different air quality levels occur.

- **AQI Level and Recommendations**

| AQI Range | Air Quality | Health Implications       | Recommendations                               |
|-----------|-------------|---------------------------|-----------------------------------------------|
| 0 - 50    | Good        | Little to no risk         | None                                          |
| 51 - 100  | Moderate    | Slight risk for sensitive individuals | Limit outdoor activity for sensitive groups |
| 101 - 150 | Unhealthy for Sensitive Groups | Risk for sensitive groups | Limit outdoor activity for sensitive groups |
| 151 - 200 | Unhealthy   | Risk for everyone         | Avoid prolonged outdoor activity             |
| 201 - 300 | Very Unhealthy | Emergency conditions  | Avoid outdoor activity                        |
| 300+      | Hazardous   | Severe health effects     | Avoid all outdoor activity                   |

  
- **Bangkok**
 
![image](https://github.com/EarthSuppawoot/air-quality/assets/157554832/80a00f9e-f7af-472a-933b-ce8c09fc614c)


- **Chiang Mai**

![image](https://github.com/EarthSuppawoot/air-quality/assets/157554832/001b6443-a8b6-4236-86b9-762c7ac35015)


- **Phuket**

![image](https://github.com/EarthSuppawoot/air-quality/assets/157554832/f5334dd9-9ecd-41f9-8392-c727ffa768f2)





