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

- Pipeline

![image](https://github.com/EarthSuppawoot/air-quality/assets/157554832/b7dd2662-9059-4798-95d7-75d083a85c66)

- DAG

![image](https://github.com/EarthSuppawoot/air-quality/assets/157554832/9e79aeb0-e7b6-4101-b711-ae52e9294cdd)

### Technologies and Tools
- Cloud: Amazon Web Services (AWS)
- Containerization: Docker
- Workflow Orchestration: Apache Airflow
- Data Lake: AWS S3
- Data Warehousing: Amazon Redshift
- Data Visualization: Power BI
- Language: Python


### Analytics Dashboard
The dashboard will have three parts with control filter on time and city that represent the analytics points below:
