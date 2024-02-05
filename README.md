# Homework 2

### Assignment

ETL pipeline that loads the data, performs some transformations, and writes the data to a database and Google Cloud!

- Link to the pipeline folder [`green_taxi_etl`](https://github.com/ch1nmay7898/DE-HW/tree/main/HW2/green_taxi_etl)
- [Data loader block](https://github.com/ch1nmay7898/DE-HW/blob/main/HW2/green_taxi_etl/api_to_python.py) that uses Pandas to read data for the final quarter of 2020 (months `10`, `11`, `12`).
- [Transformer block](https://github.com/ch1nmay7898/DE-HW/blob/main/HW2/green_taxi_etl/quarterly_data_transformer.py) that performs the following:
  - Removes rows where the passenger count is equal to 0 _or_ the trip distance is equal to zero.
  - Creates a new column `lpep_pickup_date` by converting `lpep_pickup_datetime` to a date.
  - Renames columns in Camel Case to Snake Case, e.g. `VendorID` to `vendor_id`.
  - Checks for three assertions:
    - `vendor_id` is one of the existing values in the column (currently)
    - `passenger_count` is greater than 0
    - `trip_distance` is greater than 0
- [Postgres data exporter](https://github.com/ch1nmay7898/DE-HW/blob/main/HW2/green_taxi_etl/quarterly_dataframe_to_postgres.py) written in Python, writes the dataset to the table called `green_taxi` in a schema `mage`.
    - Uses `dev` environment to connect to the Postgres instance running in the Docker container.
- [GCP data exporter](https://github.com/ch1nmay7898/DE-HW/blob/main/HW2/green_taxi_etl/df_to_parquet_gcs.py) writes the data as Parquet files to a bucket in GCP, partioned by `lpep_pickup_date`.
- [Trigger](https://github.com/ch1nmay7898/DE-HW/blob/main/HW2/green_taxi_etl/triggers.yaml) runs the pipeline daily at 5AM UTC.
