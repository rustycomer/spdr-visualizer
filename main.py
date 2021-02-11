import pandas as pd
import matplotlib.pyplot as plt


# while url != 'q':
#     user_prompt.clear_console()
#     url = user_prompt.user_input()


def get_and_clean_data():
    symbol = input("Enter SPDR Symbol: ")
    base_url = 'https://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Portfolio/Export/ExportCsv?symbol='
    spdr_url = base_url + symbol
    data = pd.read_csv(spdr_url, skiprows=1)
    data = data.replace({"%": ""}, regex=True)
    clean_data_weight = data[['Symbol', 'Weight']]
    clean_data_weight = clean_data_weight.dropna()
    clean_data_weight['Weight'] = clean_data_weight['Weight'].astype(float)
    return clean_data_weight


def produce_plot():
    data = top_ten()
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = data['Symbol']
    sizes = data['Weight']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()


def top_ten():
    data = get_and_clean_data()
    data = data.iloc[0:10]
    return data


produce_plot()

