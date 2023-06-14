import predict

ride = {
    "PULocationID": 10,
    "DOLocationID": 50,
    "trip_distance": 40
}

feats = predict.prepare_features(ride)
prediction = predict.predict(feats)

print(prediction)