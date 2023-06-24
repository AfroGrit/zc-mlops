# Monitoring

## Ratitonale

Over time, ML models may degrade. 2 effects:

1. Data Drift: new input data is no longer represented by the model's training dataset. Example: 3 new popular venues were opened in the last month, our Taxi duration model hasn't got samples of this new data in its training dataset
2. Concept Drift: In which the concept changes, i.e: The relationship between inputs and outputs has changed (Not necessarily the data itself however).This drift as the name implies is due to "concepts" (i.e: hidden variables, underpinning hypotheses..etc) changing. Example: Taxi cars have been replaced by newer, faster, nimbler cars. Our model can no longer accurately predict trip durations

| Monitor | Description |
| :--- | :--- |
|Service Health | General Software health check
| Model Performance | Depending on metrics for the problem
| Data Quality and integrity |
| Data Drift & Concept Drift |
| Performance by Segment | Performance in each segment of the input distribution
| Model bias/fairness |
| Outliers |
| Explainability |

## Batch

1. Calculate performance metrics and health metrics
2. Log the metrics in a SQL or NoSQL database
3. Build a report


## Online models

service that pulls metrics and update the dashboard in real time.

*NB* - monitor the model in Batch mode as well. 
Some issues in the model may only manifest over time or larger dataset, such as Data Drift and Concept Drift.

## Implementing Online Learning:

Batch Learning, we need three components:

1. Prediction Service
2. Evidently Service
3. MongoDB, Prometheus and Grafana



