from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)

max_value = data['target'].max()
min_value = data['target'].min()

print(f"Максимальное значение медианной стоимости: {max_value}")
print(f"Минимальное значение медианной стоимости: {min_value}")