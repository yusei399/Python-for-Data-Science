import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd

file_path_income = 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
file_path_life = 'life_expectancy_years.csv'
df_income = load(file_path_income)
df_life = load(file_path_life)

if df_income is not None and df_life is not None:
    income_1900 = df_income[['country', '1900']]
    life_1900 = df_life[['country', '1900']]
    
    income_1900.columns = ['country', 'GDP per capita (1900)']
    life_1900.columns = ['country', 'Life Expectancy (1900)']
    
    merged_data = pd.merge(income_1900, life_1900, on='country')
    
    merged_data['GDP per capita (1900)'] = merged_data['GDP per capita (1900)'].replace({'k': 'e3'}, regex=True).astype(float)
    
    plt.figure(figsize=(12, 6))
    plt.scatter(merged_data['GDP per capita (1900)'], merged_data['Life Expectancy (1900)'], label='Countries')
    
    plt.title('Life Expectancy vs GDP per Capita (1900)')
    plt.xlabel('GDP per Capita (1900)')
    plt.ylabel('Life Expectancy (1900)')
    plt.legend()
    plt.grid(True)
    
    plt.show()
else:
    print("Failed to load one or both datasets.")
