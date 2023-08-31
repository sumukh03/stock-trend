import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
scaler=MinMaxScaler(feature_range=(0,1))


def make_prediction(ticker,last_values,number_of_days,scaler=scaler):
 
    def rescale(data):
        y=scaler.inverse_transform(data)
        return y


    def get_model(ticker):
        return load_model(f"ml_models/{ticker}.h5")

    last_values=scaler.fit_transform(last_values)
    model=get_model(ticker)  
    x=np.array([last_values])
    y=[]
    for i in range(number_of_days):
        predicted=model.predict(x)
        print(predicted)
        y.append(predicted[0])
        x[0]=np.append(x[0],predicted[0])[1:].reshape(-1,1)

    return rescale(y)
