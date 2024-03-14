from airflow.decorators import dag, task
from pendulum import datetime
from fivetran_provider_async.operators import FivetranOperator

FIVETRAN_CONNECTOR_ID = "sensitize_meditation"
GITHUB_REPOSITORY = "bajaj-varun/astro-fivetran-project"
TAG_NAME = "sync-metadata"


@dag(start_date=datetime(2023, 1, 1), schedule="@daily", catchup=False)
def my_fivetran_dag():
    @task
    def upstream():
        return "Hello"

    run_fivetran_sync = FivetranOperator(
        task_id="run_fivetran_sync",
        fivetran_conn_id="fivetran",
        connector_id=FIVETRAN_CONNECTOR_ID,
    )

    @task
    def downstream():
        return "Goodbye"

    upstream() >> run_fivetran_sync >> downstream()


my_fivetran_dag()