"""
                           Задача 44: 
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""


import pandas as pd
import random

# Создаем исходный DataFrame
random.seed(42)
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем пустой DataFrame для one hot кодирования
one_hot_data = pd.DataFrame()

# Получаем уникальные значения столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Для каждого уникального значения создаем новый столбец в one hot DataFrame
for value in unique_values:
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)

# Установка опции отображения таблицы
pd.set_option('display.max_columns', None)

# Выводим one hot DataFrame
print(one_hot_data.head())
