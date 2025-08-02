import pandas as pd
from sklearn.preprocessing import StandardScaler


sc = StandardScaler()

def load_data():
    
    csv_path = "Customer-Segmentation\data\Wholesale customers data.csv"
    df = pd.read_csv(csv_path)
    df.drop(["Channel", "Region"], inplace=True)
    
    scaled_data = sc.fit_transform(df)
    
    return df, scaled_data
    