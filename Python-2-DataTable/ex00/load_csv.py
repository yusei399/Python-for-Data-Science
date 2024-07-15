import pandas as pd

def load(path: str):
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

from load_csv import load

print(load("life_expectancy_years.csv"))