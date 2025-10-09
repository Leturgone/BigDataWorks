import pandas as pd
import sns
from matplotlib import pyplot as plt
import numpy as np
from math import sqrt
import scipy.stats as stats

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
    std_val = data.std()
    min_val = data.min()
    max_val = data.max()

    print(f"\n{col.upper()}:")
    print(f"Среднее: {mean_val}")
    print(f"Медиана: {median_val}")
    print(f"Мода: {mode_val}")
    print(f"Стандартное отклонение: {std_val:.2f}")
    print(f"Мин: {min_val:.2f}, Макс: {max_val:.2f}, Разброс: {max_val - min_val:.2f}")
    print()

    axes[i].hist(data, color='green', bins=30, edgecolor='black', alpha=0.7)
    axes[i].axvline(mean_val, color='r', linestyle='--', label=f'Среднее = {mean_val:.2f}')
    axes[i].axvline(median_val, color='b', linestyle='-.', label=f'Медиана = {median_val:.2f}')
    axes[i].axvline(mode_val, color='purple', linestyle=':', label=f'Мода = {mode_val:.2f}')
    axes[i].set_title(f'Гистограмма для {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Частота')
    axes[i].legend()

plt.tight_layout()
plt.show()

# Задание 5

numeric_cols = ['age', 'bmi', 'children', 'charges']
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()  # чтобы обращаться по индексу

for i, col in enumerate(numeric_cols):
    axes[i].boxplot(df[col])
    axes[i].set_title(f'Box-plot для {col}')
    axes[i].set_ylabel('Значение')

plt.tight_layout()
plt.show()

# Задание 6

column = "charges"
n_values = [5, 50, 100]
samples = 300

# Создаем фигуру с подграфиками: по одному для каждого n
fig, axes = plt.subplots(1, len(n_values), figsize=(15, 4))

for i, n in enumerate(n_values):
    means = []

    for _ in range(samples):
        sample = df[column].sample(n, replace=True)
        means.append(sample.mean())

    mean_val = np.mean(means)
    std_val = np.std(means)

    print(f"Выборка n={n}: Cреднее = {mean_val:.2f}, std = {std_val:.2f}")

    # Строим гистограмму распределения средних
    axes[i].hist(means, bins=20, color="green", edgecolor="black", alpha=0.7)
    axes[i].set_title(f"Распределение средних (n={n})")
    axes[i].set_xlabel("Среднее значение выборки")
    axes[i].set_ylabel("Частота")
    axes[i].grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()


# Задание 7

def calc_confidence_interval(_data, confidence):
    num = len(_data)
    mean = np.mean(_data)
    std = np.std(_data, ddof=1)
    z = 1.96 if confidence == 0.95 else 2.58
    margin = z * (std / sqrt(num))
    return [float(mean - margin), float(mean + margin)]


ci_95_charges = calc_confidence_interval(df["charges"], 0.95)
ci_99_charges = calc_confidence_interval(df["charges"], 0.99)

ci_95_bmi = calc_confidence_interval(df["bmi"], 0.95)
ci_99_bmi = calc_confidence_interval(df["bmi"], 0.99)

print("\nДоверительные интервалы для charges:")
print("95%:", ci_95_charges)
print("99%:", ci_99_charges)

print("\nДоверительные интервалы для bmi:")
print("95%:", ci_95_bmi)
print("99%:", ci_99_bmi)

# Задание 8

# Признаки для проверки
features = ['bmi', 'charges']

# Процедура проверки нормальности
for feature in features:
    data = df[feature].dropna()

    print(f"\nПроверка нормальности для признака: {feature}")

    # KS-тест
    standardized_data = (data - np.mean(data)) / np.std(data, ddof=1)
    ks_stat, p_value_ks = stats.kstest(standardized_data, 'norm')
    print(f"KS-тест: статистика = {ks_stat:.4f}, p-уровень = {p_value_ks:.4f}")

    # график Q-Q
    plt.figure(figsize=(6, 4))
    stats.probplot(data, dist="norm", plot=plt)
    plt.title(f"Q-Q plot для {feature}")
    plt.show()

    # Выводы
    if p_value_ks > 0.05:
        print(f"На основе p-уровня {p_value_ks:.4f} можно не отвергать H0: данные распределены нормально.")
    else:
        print(f"На основе p-уровня {p_value_ks:.4f} отвергаем H0: данные не распределены нормально.")
