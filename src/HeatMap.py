import seaborn as sns
import matplotlib.pyplot as plt
from check_data import check_data
import pandas as pd

def heatmap_return(df, value_col='return', time_col='time', agg='sum', title='Intraday Heatmap'):
    df = df.copy()
    if len(df) > 2000:
        df = df.iloc[-2000:]
    df[time_col] = pd.to_datetime(df[time_col])
    df = df.sort_values(time_col)

    df['hour'] = df[time_col].dt.hour
    df['minute'] = df[time_col].dt.minute
    df['hour_minute'] = df['hour'].astype(str).str.zfill(2) + ":" + df['minute'].astype(str).str.zfill(2)
    df['day'] = df[time_col].dt.date

    # Créer une pivot table avec des time bins (HH:MM) sur l’axe X
    pivot = df.pivot_table(index='day', columns='hour_minute', values=value_col, aggfunc=agg)

    # Plot
    plt.figure(figsize=(14, 6))
    sns.heatmap(pivot, cmap='RdYlGn', linewidths=0.1, linecolor='grey', cbar_kws={'label': value_col})
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Day')
    plt.tight_layout()
    plt.show()

df = pd.read_csv('dataD.csv')
dfok = check_data(df)
heatmap_return(df=dfok)