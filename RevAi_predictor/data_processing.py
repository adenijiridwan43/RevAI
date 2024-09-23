import pandas as pd
from scipy import stats

def clean_and_preprocess_data(data):
    df = pd.DataFrame(data)
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.fillna(method='ffill')  # Forward fill
    
    # Remove outliers using Z-score
    for column in ['temperature', 'pressure', 'vibration']:
        df = df[(np.abs(stats.zscore(df[column])) < 3)]
    
    # Normalize numerical features
    for column in ['temperature', 'pressure', 'vibration']:
        df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    
    return df.to_dict('records')
