# mlflow, experiments & model registry

## Definitions

+ ML experiment: the process of building an ML model
+ Experiment run: each trial in an ML experiment; Each run is within an ML experiment
+ Run artifact: file associated with an ML run, model, package versions...etc;
+ Experiment metadata: experiment metadata

## Model management
### Experiment tracking

Keeping track of all the relevant information from an ML experiment

Benefits:

1. *Reproducibility*,
2. *Organization* and
3. *Optimization*

### MLflow

+ Tracking
+ Models
+ Model registry
+ Projects (Out of scope of the course)

### MLflow Tracking Client API

```python
MLFLOW_TRACKING_URI = "sqlite:///mlflow.db"
client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)
```

### MLflow Experiments

```python
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("nyc-taxi-experiment")
```

### Hyperparameter Optimizaiton Tracking

wrapping the *hyperopt* Optimization objective inside a with mlflow.

```python
def objective(params):
    with mlflow.start_run():
      # model training code
    return {'loss': rmse, 'status': STATUS_OK}

search_space = {
    'max_depth': scope.int(hp.quniform('max_depth', 4, 100, 1)),
    'learning_rate': hp.loguniform('learning_rate', -3, 0),
    # . . . 
}

best_result = fmin(
    fn=objective,
    space=search_space,
    trials=Trials()
    # . . .
```

### MLflow Autologging

```python
# globally
mlflow.autolog()
# framework-specific autologger; i.e with XGBoost:
mlflow.xgboost.autolog()
```

#### Saving Models

```python
mlflow.<framework>.log_model(model, artifact_path="models_mlflow"
```
#### Saving Artifacts with the Model

```python
mlflow.log_artifact("vectorizer.pkl", artifact_path="extra_artifacts")
```
#### Loading Models

```python
# Model UUID from the MLflow Artifact page for the run
logged_model = 'runs:/9245...00aa47/models' 
xgboost_model = mlflow.xgboost.load_model(logged_model)
```


### Model Registry
Model register does *NOT deploy models* it mainly *lists models are production ready*
create a new model registry or register the model into an existing registry

Models in the registry are labeled either as Staging, Production or Archive. 