
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
import seaborn as sns
# Задание 1

df = pd.read_csv('dataset.csv')

print("Первые 5 строк данных:")
print(df.head())
print("\nИнформация о данных:")
print(df.info())


# Кодирование категориальных переменных
label_encoders = {}
categorical_columns = ['Favorite Color', 'Favorite Music Genre', 'Favorite Beverage', 'Favorite Soft Drink']

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Кодирование целевой переменной
gender_encoder = LabelEncoder()
df['Gender'] = gender_encoder.fit_transform(df['Gender'])

print("\nДанные после кодирования:")
print(df.head())


# Задание 2

# Гистограмма баланса классов
plt.figure(figsize=(10, 6))
gender_counts = df['Gender'].value_counts()
plt.bar(['Female', 'Male'], gender_counts.values, color=['pink', 'lightblue'])
plt.title('Баланс классов в датасете', fontsize=14)
plt.xlabel('Гендер')
plt.ylabel('Количество')
plt.grid(axis='y', alpha=0.3)


# Добавление значений на столбцы
for i, count in enumerate(gender_counts.values):
    plt.text(i, count + 1, str(count), ha='center', va='bottom', fontsize=12)

plt.tight_layout()
plt.show()


# Задание 3

# Разделение на признаки и целевую переменную
X = df.drop('Gender', axis=1)
y = df['Gender']

# Разделение на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, shuffle=True,random_state=271, stratify=y)

# Масштабирование признаков
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"\nРазмер тренировочной выборки: {X_train.shape}")
print(f"Размер тестовой выборки: {X_test.shape}")

# Задание 4

# Инициализация моделей
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'SVM': SVC(kernel="rbf"),
    'KNN': KNeighborsClassifier(n_neighbors=5)
}

# Обучение и предсказание
results = {}
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for idx, (name, model) in enumerate(models.items()):
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    # Матрица ошибок
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, output_dict=True)
    print(f"\n{name}:")
    print(classification_report(y_test, y_pred))
    results[name] = report["weighted avg"]

    # Визуализация матрицы ошибок
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx],
                xticklabels=['Female', 'Male'], yticklabels=['Female', 'Male'])
    axes[idx].set_title(f'Матрица ошибок - {name}')
    axes[idx].set_xlabel('Предсказанные значения')
    axes[idx].set_ylabel('Истинные значения')

plt.tight_layout()
plt.show()

# Задание 5


# Сравнение моделей
print("СРАВНЕНИЕ РЕЗУЛЬТАТОВ КЛАССИФИКАЦИИ")

print("\nСравнение моделей по метрикам (accuracy, precision, recall, f1):")
results_df = pd.DataFrame(results).T
print(results_df[["precision", "recall", "f1-score", "support"]])

results_df[["precision", "recall", "f1-score"]].plot(kind="bar")
plt.title("Сравнение моделей по метрикам качества")
plt.ylabel("Значение метрики")
plt.xticks(rotation=0)
plt.show()