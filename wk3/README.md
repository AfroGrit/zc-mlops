# Orchestration and ML Pipelines

## 1.0 Resilience and observability

#### 1.1. decorate a task to read the data
```python
@task(retries=3, retry_delay_seconds=2)
```
#### 1.2. others, etc

```python
@task(log_prints=True)
@flow
```

*NB: take note of cashing to avoid thrashing*

## 2.0 Deploying

```terminal
prefect deploy orchestrated.py:main_flow -n taxi-duration-1 -p duration-model-pool

Deployment 'main-flow/taxi-duration-1' successfully created with id 
'3ea8cb08-a037-44fd-9617-fe71b4e7bbfa'.
View Deployment in UI: 
http://127.0.0.1:4200/deployments/deployment/3ea8cb08-a037-44fd-9617-fe71b4e7bbfa

prefect worker start -p duration-model-pool
zsh: /usr/local/bin/prefect: bad interpreter: /Users/afrogrit/miniconda3/envs/zc-de/bin/python3.9: no such file or directory
Discovered worker type 'process' for work pool 'duration-model-pool'.
Worker 'ProcessWorker c87810e8-1a3b-4471-838a-4037ea5a2bd4' started!

```