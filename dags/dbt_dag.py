import os
from datetime import datetime

from cosmos import DbtDag, ProfileConfig, ProjectConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

# profile_config = ProfileConfig(
#     profile_name="default",
#     target_name="dev",
#     profile_mapping=SnowflakeUserPasswordProfileMapping(
#         conn_id="snowflake_conn", 
#         profile_args={"database": "dbt_db", "schema": "dbt_schema"},
#         disable_event_tracking=True,
#     )
# )

# dbt_snowflake_dag = DbtDag(
#     project_config=ProjectConfig("./dags/dbt/ecom_analytics_dbt"), # Path to the DBT project directory
#     operator_args={"install_deps": True},
#     profile_config=profile_config,
#     execution_config=ExecutionConfig(dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",),
#     schedule_interval="@yearly",
#     start_date=datetime(2023, 9, 10),
#     catchup=False,
#     dag_id="dbt_dag",
# )


# Ensure the DBT project directory is relative to the Airflow home directory
dbt_project_dir = os.path.join(os.environ['AIRFLOW_HOME'], 'dags', 'dbt', 'ecom_analytics_dbt')

profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_conn", 
        profile_args={"database": "dbt_db", "schema": "dbt_schema"},
        disable_event_tracking=True,
    )
)

dbt_snowflake_dag = DbtDag(
    project_config=ProjectConfig(dbt_project_dir),
    operator_args={"install_deps": True},
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path=os.path.join(os.environ['AIRFLOW_HOME'], 'dbt_venv', 'bin', 'dbt')),
    schedule_interval="@yearly",
    start_date=datetime(2023, 9, 10),
    catchup=False,
    dag_id="dbt_dag",
)



