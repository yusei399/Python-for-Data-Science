import matplotlib  # noqa: E402
matplotlib.use("TkAgg")  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from load_csv import load  # noqa: E402


def main():
    """
    life_expectancy_years.csv と
    income_per_person_gdppercapita_ppp_inflation_adjusted.csv のデータを読み込み、
    指定した年（ここでは 1900 年）の国ごとの寿命と一人当たり所得の関係を
    散布図として表示。
    """
    try:
        life_expectancy = load("life_expectancy_years.csv")
        income_per_person = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )

        year = "1900"

        assert year in life_expectancy, (
            f"No data for year '{year}' in life expectancy"
        )
        assert year in income_per_person, (
            f"No data for year '{year}' in income per person"
        )

        year_life_expectancy = life_expectancy[year]
        year_income_per_person = income_per_person[year]

        plt.scatter(year_income_per_person, year_life_expectancy)
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=["300", "1k", "10k"])
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life expectancy")
        plt.title(year)
        plt.show()

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("Exception:", e)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
