
import time

import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from tensorflow.keras.datasets import mnist
from umap import UMAP

# Загружаем MNIST, база данных образцов рукописного написания цифр
(x_train, y_train), _ = mnist.load_data()
X = x_train.reshape((x_train.shape[0], -1))
labels = y_train


# Функция для визуализации
def plot_embedding(embedding, labels, title):
    plt.figure(figsize=(8, 6))
    #рисуем точки
    plt.scatter(embedding[:, 0], embedding[:, 1], c=labels, cmap='tab10', s=10)
    plt.title(title)
    plt.show()


# Измерение времени и выполнение UMAP с разными параметрами
umap_params = [
    {'n_neighbors': 5, 'min_dist': 0.1},
    {'n_neighbors': 30, 'min_dist': 0.3},
    {'n_neighbors': 50, 'min_dist': 0.5},
]

umap_times = []

# UMAP — это алгоритм, который умеет "сжимать" многомерные данные
# в 2D, сохраняя при этом структуру (похожие картинки оказываются рядом)
# Два ключевых параметра:
# - n_neighbors: сколько соседей учитывать
# - min_dist: насколько плотно точки могут группироваться

for params in umap_params:
    print(f"Запуск UMAP с n_neighbors={params['n_neighbors']}, min_dist={params['min_dist']}")
    start_time = time.time()
    reducer = UMAP(n_neighbors=params['n_neighbors'], min_dist=params['min_dist'], random_state=42)
    embedding = reducer.fit_transform(X) # преобразование данных в 2D
    duration = time.time() - start_time
    umap_times.append((params, duration))
    print(f"Время выполнения: {duration:.2f} секунд")
    plot_embedding(embedding, labels, f"UMAP (n_neighbors={params['n_neighbors']}, min_dist={params['min_dist']}) {duration:.2f}")

# Сравнение с t-SNE
print("\nЗапуск t-SNE для сравнения")
start_time = time.time()
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X)
tsne_duration = time.time() - start_time
print(f"t-SNE выполнен за {tsne_duration:.2f} секунд")
plot_embedding(X_tsne, labels, f"t-SNE (perplexity=30) {tsne_duration:.2f}")

# Вывод времени работы для UMAP и t-SNE
print("\nВремя работы UMAP:")
for params, t in umap_times:
    print(f"n_neighbors={params['n_neighbors']}, min_dist={params['min_dist']}: {t:.2f} секунд")
print(f"\nВремя работы t-SNE: {tsne_duration:.2f} секунд")