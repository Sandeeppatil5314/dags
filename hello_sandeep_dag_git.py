from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pendulum


with DAG(
    "hello_sandeep_dag_git",
    default_args={"retries": 2},
    description="DAG tutorial",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],

) as dag:

    def print_hello():
        print("Hello Sandeep")

    print_hello_task = PythonOperator(
        task_id="print_hello_task",
        python_callable=print_hello
    )

print_hello_task
