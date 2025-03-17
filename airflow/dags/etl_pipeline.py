from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import extract, transform, load  # Import trực tiếp các script ETL

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 3, 18),
    "retries": 1
}

dag = DAG(
    "etl_pipeline",
    default_args=default_args,
    schedule="@daily"
)

extract_task = PythonOperator(
    task_id="extract_data",
    python_callable=extract.run,  # Gọi hàm run() trong extract.py
    dag=dag
)

transform_task = PythonOperator(
    task_id="transform_data",
    python_callable=transform.run,  # Gọi hàm run() trong transform.py
    dag=dag
)

load_task = PythonOperator(
    task_id="load_data",
    python_callable=load.run,  # Gọi hàm run() trong load_to_bigquery.py
    dag=dag
)

extract_task >> transform_task >> load_task
