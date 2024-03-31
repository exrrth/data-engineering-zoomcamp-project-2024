import os
import sys
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.air_pollution_pipeline import air_quality_pipeline

default_args = {
    'owner': 'Suppawoot Kaweekijsintorn',
    'start_date': datetime(2024, 3, 18)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_aqicn_pipeline',
    default_args=default_args,
    schedule_interval='*/15 * * * *', #every 15 minute
    catchup=False,
    tags=['air_pollution', 'etl', 'pipeline']
)


locations = [
    {'latitude': 18.787746, 'longitude': 98.993126}, # Chiang Mai
    {'latitude': 13.7563305, 'longitude': 100.50176}, # Bangkok
    {'latitude': 7.884488, 'longitude': 98.39128} # Phuket
    # can add more coordinates right here
]

# extraction from aqicn
extract = PythonOperator(
    task_id='extract_from_aqicn',
    python_callable=air_quality_pipeline,
    op_kwargs={'locations': locations},
    dag=dag
)

# upload to s3
upload_to_s3 = PythonOperator(
    task_id='load_to_s3',
    python_callable=upload_s3_pipeline,
    dag=dag
)


extract >> upload_to_s3

