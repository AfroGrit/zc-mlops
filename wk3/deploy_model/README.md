# Deployments

```terminal
prefect deploy orchestrate_deploy.py:duration_main_flow -n duration_deploy_1 -p duration_deploy_pool


prefect worker start -p duration_deploy_pool

conda create --name zc-mlops-p39 python=3.9

```