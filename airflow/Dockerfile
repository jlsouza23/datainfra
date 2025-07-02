# Dockerfile
FROM apache/airflow:2.7.2-python3.10

#COPY ./dags /opt/airflow/dags
RUN pip install --upgrade pip && \
    pip install boto3 && \
    pip install dbt-core==1.9.2 && \
    pip install dbt-duckdb==1.9.2 && \
    pip install dbt-postgres==1.9.0 && \
    pip install numpy pyarrow duckdb==1.2.2