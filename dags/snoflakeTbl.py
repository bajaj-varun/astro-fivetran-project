from airflow.decorators import dag
from airflow.datasets import Dataset
from fivetran_provider_async.operators import FivetranOperator

my_snowflake_table = Dataset("snowflake://my_snowflake_conn_id/my_schema/my_table")

@dag(schedule="@daily")
def my_first_dag():
    fivetran_task = FivetranOperator(
        task_id="fivetran_task",
        connector_id="my_connector_id",
        fivetran_conn_id="my_fivetran_conn_id",
        # the outlet defines which dataset the task updates
        outlets=[my_snowflake_table],
    )

# the schedule parameter now takes a list of datasets instead of a time-based schedule
@dag(schedule=[my_snowflake_table])
def my_second_dag():
    # this dag will now run immediately after your fivetran job finishes
    pass