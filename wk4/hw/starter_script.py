#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip freeze | grep scikit-learn')


# In[2]:


import pickle
import pandas as pd


# In[3]:


with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)


# In[4]:


categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


# In[5]:


df = read_data('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-02.parquet')


# In[6]:


dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)


# In[8]:


y_pred.std()


# In[11]:


df['ride_id'] = f'{2022:04d}/{2:02d}_' + df.index.astype('str')


# In[19]:


df_result = pd.concat([df['ride_id'], pd.DataFrame(y_pred)], axis=1)
df_result.columns = ['ride_id', 'y_pred']


# In[21]:


df_result.to_parquet(
    'q2_output_file.parquet',
    engine='pyarrow',
    compression=None,
    index=False
)


# In[ ]:




