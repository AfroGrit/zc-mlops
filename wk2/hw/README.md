

### q.1

```terminal
mlflow, version 2.3.2
```

### q.2

```terminal
ls -lh
total 14208
-rw-r--r--  1 afrogrit  staff   150K May 31 22:26 dv.pkl
-rw-r--r--  1 afrogrit  staff   2.5M May 31 22:26 test.pkl
-rw-r--r--  1 afrogrit  staff   2.0M May 31 22:26 train.pkl
-rw-r--r--  1 afrogrit  staff   2.2M May 31 22:26 val.pkl
```

### q.3

```python
mlflow.sklearn.autolog()
with mlflow.start_run():
    X_train, y_train . . .

```

### q.4

