import pandas as pd
import numpy as np

# Задание 2

# Загрузка данных
data_path = 'games.csv'
df = pd.read_csv(data_path)

# Общая информация
print("Информация о данных:")
print(df.info())

print("\nПервые строки данных:")
print(df.head())

# Удаление пустых строк
df.dropna(subset=['Rating', 'Summary', 'Team'], inplace=True)

# Задание 2.1
numeric_df = df.select_dtypes(include=[np.number])

# Построение корреляционной матрицы
correlation = numeric_df.corr()

# Находим наиболее коррелирующую переменную с 'Rating'
rating_corr = correlation['Rating'].drop('Rating')
most_corr_var = rating_corr.abs().idxmax()
most_corr_value = rating_corr[most_corr_var]

print(f"Наиболее коррелирующая переменная с 'Rating': {most_corr_var} (коэффициент: {most_corr_value})")