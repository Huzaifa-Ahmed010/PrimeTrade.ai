import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

def load_data():
    fear_greed = pd.read_csv('C:\\Users\\huzai\\Downloads\\primetrade-assignment\\data\\fear_greed_index.csv')
    trades = pd.read_csv('C:\\Users\\huzai\\Downloads\\primetrade-assignment\\data\\historical_data.csv')
    return fear_greed, trades

def clean_data(fear_greed, trades):
    fear_greed['date'] = pd.to_datetime(fear_greed['date']).dt.date

    trades['Timestamp IST'] = pd.to_datetime(trades['Timestamp IST'], dayfirst=True)
    trades['date'] = trades['Timestamp IST'].dt.date
    return fear_greed, trades

def merge_data(fear_greed, trades):
    merged = trades.merge(fear_greed, on='date', how='left')
    return merged

def analyze(merged):

    merged['win'] = merged['Closed PnL'] > 0

    print(f"\n Average PnL by Sentiment: {merged.groupby('classification')['Closed PnL'].mean()}")
    print(f"\n Win Rate by Sentiment:{merged.groupby('classification')['win'].mean()}")
    print(f"\n Leverage by Sentiment: {merged.groupby('classification')['Size USD'].mean()}")

def visualize(merged):

    pnl = merged.groupby('classification')['Closed PnL'].mean()
    pnl = merged.groupby('classification')['Closed PnL'].mean().sort_values()
    sbn.barplot(x=pnl.index, y=pnl.values)
    plt.title("Average PnL by Sentiment")
    plt.xticks(rotation=45)
    plt.show()

def main():
    fear_greed, trades = load_data()
    fear_greed, trades = clean_data(fear_greed, trades)
    merged = merge_data(fear_greed, trades)

    analyze(merged)
    visualize(merged)

if __name__ == "__main__":
    main()
