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

# Задание 4

cols = ['bmi', 'charges']
n_cols = len(cols)

fig, axes = plt.subplots(1, n_cols, figsize=(14, 6))

for i, col in enumerate(cols):
    data = df[col]
    mean_val = data.mean()
    median_val = data.median()
    mode_val = data.mode()[0]
    std_dev = data.std()

    print(f"\n{col.upper()}:")
    print(f"Среднее: {mean_val}")
    print(f"Медиана: {median_val}")
    print(f"Мода: {mode_val}")

    axes[i].hist(data, bins=20, edgecolor='black', alpha=0.7)
    axes[i].axvline(mean_val, color='r', linestyle='--', label=f'Среднее = {mean_val:.2f}')
    axes[i].axvline(median_val, color='g', linestyle='-.', label=f'Медиана = {median_val:.2f}')
    axes[i].axvline(mode_val, color='purple', linestyle=':', label=f'Мода = {mode_val:.2f}')
    axes[i].set_title(f'Гистограмма для {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Частота')
    axes[i].legend()

plt.tight_layout()
plt.show()

# Задание 5
