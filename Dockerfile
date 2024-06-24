FROM quay.io/astronomer/astro-runtime:11.5.0

# create environment and install dbt
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-snowflake && deactivate
