import matplotlib                      # noqa: E402
matplotlib.use("TkAgg")                # noqa: E402
import matplotlib.pyplot as plt        # noqa: E402
from load_csv import load


def main():
    file_path = 'life_expectancy_years.csv'
    df = load(file_path)

    if df is not None:
        country = 'France'
        country_data = df[df['country'] == country].T
        country_data = country_data[1:]
        country_data.columns = ['Life Expectancy']

        country_data.index = country_data.index.astype(int)

        plt.figure(figsize=(10, 5))
        plt.plot(
            country_data.index,
            country_data['Life Expectancy'],
            label=country
        )
        plt.title(f'Life Expectancy Over Time for {country}')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.legend()
        plt.grid(True)

        xticks = list(
            range(
                country_data.index.min(),
                country_data.index.max() + 1,
                40
            )
        )
        plt.xticks(xticks)

        plt.show()
    else:
        print("Failed to load dataset.")


if __name__ == "__main__":
    main()
