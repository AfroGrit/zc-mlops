# Homework #3 - Orchestration

### Q1. Human-readable name

formating logs 

```python
@task(retries=3, retry_delay_seconds=2, name="Read taxi data")
Flow run 'amusing-armadillo' - Created task run 'Read taxi data-0' for task 'Read taxi data'
```

### Q2. Cron

0 9 3 * *

```terminal
prefect deploy wk3/hw/orchestrated_hw.py:duration_deploy_flow_hw -n taxi-duration-deploy-hw -p duration-model-deploy-hw-pool
prefect worker start -p duration-model-deploy-hw-pool
```

note - https://crontab.guru/

### Q3. RMSE

```terminal
INFO  [prefect.task_runs] [97]  validation-rmse:4.21665
INFO  [prefect.task_runs] [98]  validation-rmse:4.21547
INFO  [prefect.task_runs] [99]  validation-rmse:4.21354
```

### Q4. RMSE (Markdown Artifact)

```Markdown
    ## Summary
    Duration Prediction 
    ## RMSE XGBoost Model
    | Region    | RMSE |
    |:----------|-------:|
    | 2023-06-12 | 5.37 |
    
```
### Q5. Emails

```python
email_send_message
```
### Q6. Prefect Cloud
