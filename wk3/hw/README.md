# Homework #3 - Orchestration

### Q1. Human-readable name

formating logs 

```python
@task(retries=3, retry_delay_seconds=2, name="Read taxi data")
Flow run 'amusing-armadillo' - Created task run 'Read taxi data-0' for task 'Read taxi data'
```

### Q2. Cron


```terminal
prefect deploy wk3/hw/orchestrated_hw.py:duration_deploy_flow_hw -n taxi-duration-deploy-hw -p duration-model-deploy-hw-pool
prefect worker start -p duration-model-deploy-hw-pool
```

### Q3. RMSE
### Q4. RMSE (Markdown Artifact)
### Q5. Emails
### Q6. Prefect Cloud
