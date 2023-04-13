import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Словарь для one-hot
categories = list(set(lst))
cat_dict = {}
for i, category in enumerate(categories):
    cat_dict[category] = [0] * i + [1] + [0] * (len(categories) - i - 1)

# Преобразуем DataFrame в one-hot DataFrame
one_hot_df = pd.DataFrame()
for index, row in data.iterrows():
    series = pd.Series(cat_dict[row['whoAmI']])
    series.index = categories
    one_hot_df = pd.concat([one_hot_df, series], axis=1)

one_hot_df = one_hot_df.T.reset_index(drop=True)
print(one_hot_df)
