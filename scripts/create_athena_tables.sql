CREATE DATABASE IF NOT EXISTS customer360_athena;

-- Curated Customer360 Table
CREATE EXTERNAL TABLE IF NOT EXISTS customer360_athena.curated_customer360 (
    customer_id STRING,
    email STRING,
    first_name STRING,
    last_name STRING,
    total_clicks INT,
    last_login TIMESTAMP,
    churn_score DOUBLE,
    registration_date DATE
)
PARTITIONED BY (year STRING, month STRING)
STORED AS PARQUET
LOCATION 's3://customer360-data-lake/curated/customer360/'
TBLPROPERTIES ("parquet.compress"="SNAPPY");

MSCK REPAIR TABLE customer360_athena.curated_customer360;

-- Daily Snapshot Table
CREATE EXTERNAL TABLE IF NOT EXISTS customer360_athena.daily_snapshot (
    snapshot_date DATE,
    total_customers INT,
    avg_churn_score DOUBLE,
    active_users INT
)
STORED AS PARQUET
LOCATION 's3://customer360-data-lake/exports/daily_snapshot/'
TBLPROPERTIES ("parquet.compress"="SNAPPY");

-- CRM Cleaned Table
CREATE EXTERNAL TABLE IF NOT EXISTS customer360_athena.clean_crm (
    customer_id STRING,
    email STRING,
    first_name STRING,
    last_name STRING,
    phone STRING,
    region STRING,
    source STRING
)
STORED AS PARQUET
LOCATION 's3://customer360-data-lake/staging/clean/crm/';
