import pandas as pd
import numpy as np


def most_medals(data):
    d = pd.DataFrame(data)
    d = d.groupby(['Name'], as_index=False).agg('count').sort_values('Medal', ascending=False)
    # d = d[d.Medal != 0]
    name = (d.iloc[:5])
    # d = data.loc[data['Name'].isin(name['Name'])]
    print(d[['Name', 'Sport', 'NOC', 'Medal']])


def players_with_gold_medals(data):
    d = pd.DataFrame(data)