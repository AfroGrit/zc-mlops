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

## q4. Monitoring

## q5. Dashboard