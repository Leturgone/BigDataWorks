import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from tensorflow.keras.datasets import mnist
import time

# Загружаем MNIST
(x_train, y_train), _ = mnist.load_data()
X = x_train.reshape((x_train.shape[0], -1))
labels = y_train

# Функция для отображения результатов
def plot_tsne(embedding, labels, perplexity):
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(embedding[:, 0], embedding[:, 1], c=labels, cmap='tab10', s=10)
    plt.legend(*scatter.legend_elements(), title="Digits")
    plt.title(f't-SNE с perplexity={perplexity}')
    plt.show()

# Переменные для хранения времени выполнения
times = []

# Разные значения perplexity
perplexity_values = [5, 30, 50]

for perplexity in perplexity_values:
    print(f"\nЗапуск t-SNE с perplexity={perplexity}")
    start_time = time.time()
    tsne = TSNE(n_components=2, perplexity=perplexity, random_state=42)
    embedding = tsne.fit_transform(X)
    duration = time.time() - start_time
    times.append((perplexity, duration))
    print(f"Время выполнения: {duration:.2f} секунд")
    plot_tsne(embedding, labels, perplexity)

# Вывод времени выполнения для каждого perplexity
print("\nВремя выполнения для разных perplexity:")
for p, t in times:
    print(f"Perplexity={p}: {t:.2f} секунд")