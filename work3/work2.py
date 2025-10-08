import pandas as pd


# Задание 9

data_path = 'ECDCCases.csv'
df = pd.read_csv(data_path)

# Задание 10

# Проверка пропусков и подсчет процентов
missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100
print(missing_percent)

# Удаление двух признаков с наибольшим числом пропусков
cols_to_drop = missing.sort_values(ascending=False).head(2).index
print("Удаляем признаки:", cols_to_drop)
df = df.drop(columns=cols_to_drop)

# Разделение признаков на категориальные и числовые
cat_cols = df.select_dtypes(include="object").columns
num_cols = df.select_dtypes(exclude="object").columns

# Заполнение оставшихся пропусков
for col in cat_cols:
    df[col] = df[col].fillna("other")

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Проверка, что пропусков нет
print(df.isnull().sum())
