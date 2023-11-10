from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator


default_args={
    'owner':"Toema",
    'retries':5,
    'retry_delay':timedelta(minutes=10)

}

with DAG(
    dag_id="fetch_google_data_v03",
    default_args=default_args,
    start_date=datetime(2023, 11, 2),
    schedule='@daily'
) as dag:
    
    task1=BashOperator(
        task_id="1st_task",
        bash_command="ls"
    )
    task14=BashOperator(
        task_id="14th_task",
        bash_command="pip install wget"
    )
    task2=BashOperator(
        task_id="2nd_task",
        bash_command="cd /opt/airflow/dags"
    )
    task4=BashOperator(
        task_id="4th_task",
        bash_command="cd /opt/airflow/dags/src/scripts/"
    )
    task5=BashOperator(
        task_id="5th_task",
        bash_command="pwd"
    )
    task3=BashOperator(
        task_id="3rd_task",
        bash_command="python /opt/airflow/dags/src/scripts/fetch_automatic_downloads.py"
    )
    # task3=PythonOperator(
    #     task_id="3rd_task",
    #     python_callable=fetch_automatic_downloads.fetch_automatic_downloads
    # )
    task1>>task14>>task2>>task3>>task4>>task5