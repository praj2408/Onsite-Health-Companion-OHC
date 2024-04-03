
import pickle
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler


# Diabetes prediction

def diabetes_prediction(data):
    
    with open("src/Diabetes-Detection/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)

    data = np.array(data).reshape(1,-1)
    scaled_data = scaler.transform(data)
    
    with open("src/Diabetes-Detection/model.pkl", "rb") as f:
        model = pickle.load(f)
        
    pred = model.predict(scaled_data)
    
    
    return pred

# new_data = np.array([6,148,72,35,0,33.6,0.627,50]).reshape(1, -1)

# pred = diabetes_prediction(new_data)

# if pred==1:
#     print("The patient has diabetes")