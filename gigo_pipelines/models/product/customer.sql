{{ config(materialized='table') }}

select *
from postgres_scan('postgres', 'public', 'customer')
