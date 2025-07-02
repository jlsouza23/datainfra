from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

def executar_dump():
    # Aqui você pode substituir por pg_dump, export CSV, etc.
    logging.info("Executando dump de dados...")
    # Simulação de dump:
    with open("/tmp/backup_simulado.csv", "w") as f:
        f.write("id,nome,email\n1,João,joao@example.com\n2,Maria,maria@example.com")
    logging.info("Dump concluído e salvo em /tmp/backup_simulado.csv")

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="dag_dump_exemplo",
    default_args=default_args,
    schedule_interval="0 2 * * *",  # todos os dias às 02:00
    catchup=False,
    description="DAG de exemplo para simular um dump de dados"
) as dag:

    dump_task = PythonOperator(
        task_id="executar_dump",
        python_callable=executar_dump
    )

    dump_task
