import sys
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

WORKDIR = os.path.dirname('/opt/app/')
sys.path.insert(0, WORKDIR)

from auchan_file_process.process_files import process_files
from auchan_file_process.settings import Settings

setting = Settings()


def process_files_airflow(directory_paths, **kwargs):
    process_files(directory_paths)


dag = DAG(
    'process_files_dag',
    default_args={
        'owner': 'valentin',
        'depends_on_past': False,
        'start_date': datetime(2024, 3, 13),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    tags=["test"],
    description='Process files in directories',
    schedule_interval=timedelta(days=1),
)

process_files_task = PythonOperator(
    task_id='process_files_task',
    python_callable=process_files_airflow,
    op_kwargs={'directory_paths': setting.input_dir},
    dag=dag,
)



