# AIR Quality Data Project

### Problem Statement
The project aim to build end-to-end data pipeline that extract air quality data from api. The extracted data will be processed and enri

### Running pipeline (DAG)
- dag update every 20 minutes to update the data that become uptodate normally data will be update hourly but there is a delay

### Technologies and Tools
- Cloud - AWS
- Containerization - Docker,Docker Compose
- Workflow Orchestration - Apache Airflow
- Data Lake - AWS S3
- Data Visualization - Power BI
- Language - Python

### Analytics Dashboard
The dashboard will have three parts with control filter on time and city that represent the analytics points below:

- 

### Data schema
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

