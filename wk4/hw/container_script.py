import sys
import pickle
import pandas as pd

# CLI consfiguration = Run the script for March 2022.

year = int(sys.argv[1]) # 2022
month = int(sys.argv[2]) #3

source = f'https://d37ci6vzurychx.cloudfront.net/trip-data'
input_file = f'{source}/yellow_tripdata_{year:04d}-{month:02d}.parquet'
output_file = f'data/{year:04d}_{month:02d}_predictions.parquet'


with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


df = read_data(input_file)
df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')


dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)

print(f'predicted mean duration date {year}/{month} :, {y_pred.mean()}')


df_result = pd.concat([df['ride_id'], pd.DataFrame(y_pred)], axis=1)
df_result.columns = ['ride_id', 'y_pred']



