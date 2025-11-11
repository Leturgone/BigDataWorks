import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Задание 2

# Загрузка данных
data_path = 'games.csv'
df = pd.read_csv(data_path)

# Общая информация
print("Информация о данных:")
print(df.info())



# Удаление пустых строк
df.dropna(subset=['Rating', 'Summary', 'Team'], inplace=True)

# Обработка числовых признаков с 'K'
def convert_to_numeric(value):
    if pd.isnull(value):
        return np.nan
    value = str(value).replace(',', '').strip()
    if 'K' in value:
        return float(value.replace('K', '')) * 1_000
    else:
        return float(value)

# Применим к нужным колонкам
numeric_cols = ['Times Listed', 'Number of Reviews', 'Plays','Playing', 'Backlogs','Wishlist']
for col in numeric_cols:
    df[col] = df[col].apply(convert_to_numeric)

print("\nПервые строки данных:")
print(df.head(2))


# Задание 2.1

target_col = 'Rating'
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr(numeric_only=True)[target_col].drop(target_col).sort_values(key=lambda s: s.abs(), ascending=False)

print(f"\nКорреляции с целевой переменной '{target_col}':\n", corr)
top_feature = corr.index[0]
print(f"\nНаиболее коррелирующий признак: {top_feature} (r = {corr.iloc[0]:.3f})")


# Задание 2.2

# Выбираем наиболее коррелирующий признак
feature = top_feature

# Подготовка данных для регрессии
x = numeric_df[top_feature].values
y = numeric_df[target_col].values

# Нормализация признака
x_mean, x_std = x.mean(), x.std()
x_norm = (x - x_mean) / x_std

# Инициализация параметров
w0, w1 = 0.0, 0.0
learning_rate = 0.001
eps = 1e-8
max_iterations = 100000

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Градиентный спуск
prev_loss = np.inf
converged_at = max_iterations

for i in range(max_iterations):
    # Прямое распространение
    y_pred = w1 * x_norm + w0
    # Ошибка
    error = y - y_pred
    # Градиенты
    dw0 = (-2 / len(x)) * np.sum(error)
    dw1 = (-2 / len(x)) * np.sum(error * x_norm)
    # Обновление параметров
    w0 -= learning_rate * dw0
    w1 -= learning_rate * dw1
    # Проверка сходимости
    current_loss = mse(y, y_pred)
    if abs(prev_loss - current_loss) < eps:
        converged_at = i
        break
    prev_loss = current_loss

# Преобразование параметров обратно в исходную шкалу
w1_orig = w1 / x_std
w0_orig = w0 - w1 * x_mean / x_std

# Финальная MSE на исходных данных
final_mse = mse(y, w1_orig * x + w0_orig)


print(f"\nРучная линейная регрессия")
print(f"Наклон (w1): {w1_orig:.6f}")
print(f"Сдвиг (w0): {w0_orig:.6f}")
print(f"MSE: {final_mse:.6f}")

# Задание 2.3

# Построение графика
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.6, label='Данные')
x_line = np.linspace(x.min(), x.max(), 100)
y_line = w1_orig * x_line + w0_orig
plt.plot(x_line, y_line, color='red', linewidth=2, label='Линейная регрессия')
plt.xlabel(top_feature)
plt.ylabel(target_col)
plt.title(f'Линейная регрессия: {target_col} ~ {top_feature}\n')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()