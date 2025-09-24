
import matplotlib.pyplot as plt
import time
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
from umap import UMAP
from sklearn.manifold import TSNE

# Загружаем MNIST (или Fashion MNIST по желанию)
mnist = fetch_openml('mnist_784', version=1)
X = mnist.data
labels = mnist.target.astype(int)

# Можно предварительно уменьшить размерность с помощью PCA для ускорения
pca = PCA(n_components=50, random_state=42)
X_reduced = pca.fit_transform(X)

# Функция для визуализации
def plot_embedding(embedding, labels, title):
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(embedding[:, 0], embedding[:, 1], c=labels, cmap='tab10', s=10)
    plt.legend(*scatter.legend_elements(), title="Digits")
    plt.title(title)
    plt.show()

# Измерение времени и выполнение UMAP с разными параметрами
umap_params = [
    {'n_neighbors': 15, 'min_dist': 0.1},
    {'n_neighbors': 50, 'min_dist': 0.5},
    {'n_neighbors': 30, 'min_dist': 0.3}
]

umap_times = []

for params in umap_params:
    print(f"Запуск UMAP с n_neighbors={params['n_neighbors']}, min_dist={params['min_dist']}")
    start_time = time.time()
    reducer = UMAP(n_neighbors=params['n_neighbors'], min_dist=params['min_dist'], random_state=42)
    embedding = reducer.fit_transform(X_reduced)
    duration = time.time() - start_time
    umap_times.append((params, duration))
    print(f"Время выполнения: {duration:.2f} секунд")
    plot_embedding(embedding, labels, f"UMAP (n_neighbors={params['n_neighbors']}, min_dist={params['min_dist']})")

# Теперь сравним с t-SNE
print("\nЗапуск t-SNE для сравнения")
start_time = time.time()
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X_reduced)
tsne_duration = time.time() - start_time
print(f"t-SNE выполнен за {tsne_duration:.2f} секунд")
plot_embedding(X_tsne, labels, "t-SNE (perplexity=30)")

# Вывод времени работы для UMAP и t-SNE
print("\nВремя работы UMAP:")
for params, t in umap_times:
    print(f"n_neighbors={params['n_neighbors']}, min_dist={params['min_dist']}: {t:.2f} секунд")
print(f"\nВремя работы t-SNE: {tsne_duration:.2f} секунд")