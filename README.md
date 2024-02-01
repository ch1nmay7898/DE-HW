# Homework 1

## Question 1. Knowing docker tags

### Process
```
docker run --help

--rm     Automatically remove the container when it exits
```


## Question 2. Understanding docker first run 

### Process

- Create Dockerfile in the current directory
  ```
  FROM python:3.9
  ENTRYPOINT [ "bash"]
  ```
- Run the following in the current directory
  ```
  docker build -t homeworktest .
  docker run -it 
  ```
- Run the following in the docker container
  ```
  pip list
  ```
  Output:
  ```
  Package    Version
  ---------- -------
  pip        23.0.1
  setuptools 58.1.0
  wheel      0.42.0
  ```

## Question 3. Count records 

### SQL Query
```
SELECT COUNT(*)
FROM green_taxi_trips g
WHERE g.lpep_pickup_datetime::date = '2019-09-18'::date
AND g.lpep_dropoff_datetime::date = '2019-09-18'::date;
```
Output:
15612

## Question 4. Longest trip for each day

### SQL Query
```
SELECT g.lpep_pickup_datetime::date
FROM green_taxi_trips g
WHERE g.Trip_distance = (SELECT MAX(Trip_distance) FROM green_taxi_trips);
```
Output:
2019-09-26

## Question 5. Three biggest pick up Boroughs

### SQL Query
```
SELECT s."Borough" FROM (SELECT z."Borough", SUM(g."total_amount") as borough_sum
FROM "green_taxi_trips" g
LEFT JOIN "zone_data" z ON z."LocationID" = g."PULocationID"
WHERE g."lpep_pickup_datetime"::date = '2019-09-18'::date
GROUP BY z."Borough") s
WHERE s."borough_sum" > 50000;
```
Output:

Borough

Brooklyn
Manhattan
Queens


## Question 6. Largest tip

### SQL Query
```
SELECT z1."Zone" FROM "zone_data" z1
WHERE z1."LocationID" = (SELECT g."DOLocationID"
FROM "green_taxi_trips" g
LEFT JOIN "zone_data" z ON z."LocationID" = g."PULocationID"
WHERE z."Zone" = 'Astoria'
ORDER BY g."tip_amount" DESC
LIMIT 1);
```
Output:
Zone

JFK Airport
