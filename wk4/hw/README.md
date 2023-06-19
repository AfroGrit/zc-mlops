# Deplyments - homework

## Q1. Notebook
You can find the initial notebook here.

Run this notebook for the February 2022 data.

What's the standard deviation of the predicted duration for this dataset?
```python
y_pred.std()
5.28140357655334
```

## Q2. Preparing the output

```terminal
ls -lh
-rw-r--r--  1 afrogrit  staff    57M Jun 19 13:11 q2_output_file.parquet
```

## Q3. Creating the scoring script
Which command you need to execute for that?
```terminal
jupyter nbconvert starter.ipynb --to python
```

## Q5. Parametrize the script

```terminal
python param_script.py 2022 3
predicted mean duration: 12.758556818790902
```

save predictions in data dir

## Q6. Docker container

What's the mean predicted duration for April 2022?

```terminal
 => => writing image sha256:.0438a56adfa238680a4 0.0s
 => => naming to docker.io/library/ride-duration-prediction-service:hw  0.0s
✗ ✗ docker run -it --rm ride-duration-prediction-service:hw 2022 4                  
predicted mean duration date 2022/4 :, 12.827242870079969
```