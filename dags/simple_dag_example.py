# Simplest possible airflow dag creation
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

def py_func(x: str):
    print("python function invoked from airflow")
    print("Message:: "+x)

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['mail.abhishek.kushwaha@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

with DAG(
    'simple-dag-example',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 1, 15),
    catchup=False,
    tags=['simplest','simple']) as dag:
    
    task1 = BashOperator(task_id = 'show-time', bash_command = 'time')
    task2 = BashOperator(task_id = 'show-date', bash_command = 'date')
    task3 = PythonOperator(task_id = 'Python-Operate', 
                           python_callable=py_func,
                           op_kwargs={"x" : "Hello Airflow Welcome!!"})
    
    task1 >> task2 >> task3
