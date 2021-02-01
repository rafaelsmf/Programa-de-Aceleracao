from airflow import DAG
from airflow.operators import BaseOperator
from datetime import timedelta, datetime


default_args = {
    "depends_on_past": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
    dag_id="project1",
    default_args=default_args,
    description="Números da Covid-19 no Brasil",
    schedule_interval="@daily",
    start_date=datetime(2020, 2, 26)
)

start_execution_task = BaseOperator(
    task_id="start_execution"
)

# TODO: implement StageToS3Operator
stage_to_s3_task = BaseOperator(
    task_id="stage_to_s3"
)

# TODO: implement check quality function
check_quality_task = BaseOperator(
    task_id="check_quality"
)

# TODO: implement perform analysis function
perform_analysis_task = BaseOperator(
    task_id="perform_analysis"
)

end_execution_task = BaseOperator(
    task_id="end_execution"
)

start_execution_task >> stage_to_s3_task
stage_to_s3_task >> check_quality_task
check_quality_task >> perform_analysis_task
perform_analysis_task >> end_execution_task