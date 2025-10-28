import numpy as np
import matplotlib.pyplot as plt

# Векторы данных
street = np.array([80, 98, 75, 91, 78])
garage = np.array([100, 82, 105, 89, 102])

# 1. Расчет корреляции по Пирсону
r = np.corrcoef(street, garage)[0, 1]
print(f"Коэффициент корреляции r: {r:.2f}")

# 2. Построение диаграммы рассеяния
plt.scatter(street, garage)
plt.title("Диаграмма рассеяния")
plt.xlabel("Улица")
plt.ylabel("Гараж")
plt.grid(True)
plt.show()
