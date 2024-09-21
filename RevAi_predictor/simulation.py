from django.shortcuts import render
import pandas as pd
import numpy as np

def simulate_sensor_data(days=30):
    date_range = pd.date_range(end=pd.Timestamp.now(), periods=days)
    temperatures = np.random.normal(30, 5, days)
    vibrations = temperatures * 2 + np.random.normal(0, 10, days)
    return pd.DataFrame({
        'timestamp': date_range,
        'temperature': temperatures,
        'vibration': vibrations
    })