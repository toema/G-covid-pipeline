from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor

from airflow.hooks.S3_hook import S3Hook

default_args={
    'owner':"Toema",
    'retries':5,
    'retry_delay':timedelta(minutes=10)

}


def load_to_s3():
    s3_hook=S3Hook(aws_conn_id="s3_minio_conn")
    s3_hook.load_file(filename="dags/data/exports/cc_by/aggregated_cc_by.csv",
                      key="exports/aggregated_cc_by.csv",
                      bucket_name="c19",
                      replace=True)

with DAG(
    dag_id="check_S3_minio_bucket_v02",
    default_args=default_args,
    start_date=datetime(2023, 11, 2),
    schedule='@daily',
    catchup=False
) as dag:
    
    task1=BashOperator(
        task_id="1st_task",
        bash_command="pip install minio "
    )
    task2=BashOperator(
        task_id="2nd_task",
        bash_command="pip install urllib3"
    )

    task12=S3KeySensor(
        task_id="12st_task",
        bucket_name="c19",
        aws_conn_id="s3_minio_conn",
        bucket_key="country_wise_latest.csv"
    )
    
    task4=PythonOperator(
        task_id="4th_task",
        python_callable=load_to_s3
    )
    
    task1>>task2>>task12>>task4