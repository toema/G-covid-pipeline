from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
\

default_args={
    'owner':"Toema",
    'retries':5,
    'retry_delay':timedelta(minutes=10)

}

with DAG(
    dag_id="export_google_data_v02",
    default_args=default_args,
    start_date=datetime(2023, 11, 2),
    schedule='@daily'
) as dag:
    
    # task1=BashOperator(
    #     task_id="task1",
    #     bash_command="ls"
    # )
    # task2=BashOperator(
    #     task_id="2nd_task2",
    #     bash_command="cd /opt/airflow/dags/pathToOpenCovid19.lnk"
    # )
    task2=BashOperator(
        task_id="2nd_task",
        bash_command="pwd"
    )
    task3=BashOperator(
        task_id="3rd_task",
        bash_command="python /opt/airflow/dags/src/scripts/export_data.py"
    )
    # task3=PythonOperator(
    #     task_id="3rd_task",
    #     python_callable=fetch_automatic_downloads.fetch_automatic_downloads
    # )
    task2>>task3