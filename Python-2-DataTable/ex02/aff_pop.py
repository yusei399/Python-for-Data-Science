import matplotlib.pyplot as plt
from load_csv import load

# Load the dataset
file_path = 'population_total.csv'
df = load(file_path)

if df is not None:
    countries = ['France', 'Japan']
    plt.figure(figsize=(12, 6))
    
    for country in countries:
        country_data = df[df['country'] == country].T
        country_data = country_data[1:]
        country_data.columns = ['Population']
        country_data.index = country_data.index.astype(int)
        country_data['Population'] = country_data['Population'].replace({'M': 'e6', 'k': 'e3'}, regex=True).astype(float)
        
        plt.plot(country_data.index, country_data['Population'], label=country)
    
    plt.title('Population Over Time')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.legend()
    plt.grid(True)
    
    xticks = list(range(1800, 2051, 40))
    plt.xticks(xticks)
    
    yticks = list(range(0, int(country_data['Population'].max()) + 1, 20000000))
    plt.yticks(yticks, [f'{int(y/1e6)}M' for y in yticks])
    
    plt.show()
else:
    print("Failed to load dataset.")
