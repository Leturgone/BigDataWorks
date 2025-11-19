
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Задание 1

df = pd.read_csv('dataset.csv')

print("Первые 5 строк данных:")
print(df.head())
print("\nИнформация о данных:")
print(df.info())

