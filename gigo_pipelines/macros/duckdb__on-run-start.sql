{% macro duckdb__on_run_start() %}
  ATTACH 'postgresql://postgres:postgres@0.0.0.0:5432/postgres' 
  AS postgres 
  (TYPE postgres);
{% endmacro %}