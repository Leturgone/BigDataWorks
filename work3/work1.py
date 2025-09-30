import pandas as pd
import sns
from matplotlib import pyplot as plt

# Задание 1

data_path = 'insurance.csv'
df = pd.read_csv(data_path)

# Задание 2

desc = df.describe()
print("Статистика по данным:\n", desc)

# Задание 3

numeric_cols = ['age', 'bmi', 'children', 'charges']
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()  # чтобы обращаться по индексу

for i, col in enumerate(numeric_cols):
    axes[i].hist(df[col], color='green', bins=30, edgecolor='black', alpha=0.7)
    axes[i].set_title(f'Гистограмма для {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Частота')

plt.tight_layout()
plt.show()


