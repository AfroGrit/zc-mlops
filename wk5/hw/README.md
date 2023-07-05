# Homework - Monitoring

## q1. Prepare the dataset

```python
mar_data.shape
(72044, 20)
```

## q2. Metric

```python
report = Report(metrics=[
    ColumnDriftMetric(column_name='prediction'),
    DatasetDriftMetric(),
    DatasetMissingValuesMetric(),
    ColumnQuantileMetric(column_name="fare_amount", quantile=0.5),
    RegressionPerformanceMetrics()
]
)
```

## q3. Prefect flow

```python
@task(retries=2, retry_delay_seconds=5, name="calculate metrics")
Created task run 'calculate metrics-0' for task 'calculate metrics'
```
## q4. Monitoring

```python
result['metrics'][3]['result']
{'column_name': 'fare_amount',
 'column_type': 'num',
 'quantile': 0.5,
 'current': {'value': 12.8},
 'reference': {'value': 12.8}}
 ```

## q5. Dashboard

```terminal
project_folder/dashboards (05-monitoring/dashboards)
```