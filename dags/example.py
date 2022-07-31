import json

from airflow import DAG
from airflow.operators.empty import EmptyOperator

from plugins.selenium_plugin.operators.selenium_operator import SeleniumOperator
from scripts.selenium_scripts.example import example_task
from datetime import datetime, timedelta
from airflow.models import Variable

default_args = {
    'owner': 'brayan.correa',
    # 'wait_for_downstream': True,
    'start_date': datetime(2021, 6, 22),
    'retries': 0,
    'retries_delay': timedelta(minutes=5)
}

dag = DAG(
    'example_task',
    schedule_interval=None,
    default_args=default_args, concurrency=2
)

start = EmptyOperator(
    task_id='start',
    dag=dag
)

processed = SeleniumOperator(
    script=example_task,
    script_args=[],
    task_id='processed',
    dag=dag
)

end = EmptyOperator(
    task_id='end',
    dag=dag,
)

start >> processed >> end
