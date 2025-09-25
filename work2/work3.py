import pandas as pd
import matplotlib.pyplot as plt


def convert_players(val):
    if isinstance(val, str):
        if 'K' in val:
            number = float(val.replace('K', ''))
            return number * 1000
        else:
            try:
                return float(val)
            except:
                return None
    else:
        return val


# Загрузка данных
data_path = 'games.csv'
df = pd.read_csv(data_path)

# Удаление пустых строк
df.dropna(subset=['Rating', 'Summary', 'Team'], inplace=True)

# Преобразуем параметры в числовой тип
df['Playing'] = df['Playing'].apply(convert_players)
df['Rating'] = df['Rating'].astype(float)
df['ReleaseYear'] = pd.to_datetime(df['Release Date'], errors='coerce').dt.year

# Группируем по году и считаем средний рейтинг и среднее количество игроков
avg_stats_per_year = df.groupby('ReleaseYear').agg({
    'Rating': 'mean',
    'Playing': 'max'
}).sort_index()



# Построение графика с годом выхода и  рейтингом

plt.figure(figsize=(12, 6))
plt.plot(avg_stats_per_year.index, avg_stats_per_year['Rating'],
         marker='o',
         markerfacecolor="white", # цвет точек
         markeredgecolor="black", # цвет границы
         markeredgewidth=2, # толщина границы
         color='crimson',
         linestyle='-',
         label='Средний рейтинг')

plt.xlabel('Год выхода', fontsize=14)
plt.ylabel('Средний рейтинг', fontsize=14)
plt.title('Средний рейтинг по годам выхода игр', fontsize=20)
plt.grid(True, linewidth=2, color="mistyrose")
plt.legend()
plt.show()

# Построение графика c годом выхода игры и кол-вом игроков в текущий момент
plt.figure(figsize=(12, 6))
plt.plot(avg_stats_per_year.index, avg_stats_per_year['Playing'],
         marker='o',
         markerfacecolor="white", # цвет точек
         markeredgecolor="black", # цвет границы
         markeredgewidth=2, # толщина границы
         color='blue',
         linestyle='-',
         label='Максимальное количество игроков')
plt.xlabel('Год выхода',fontsize=14)
plt.ylabel('Максимальное количество игроков',fontsize=14)
plt.title('Максимальное количество игроков по году', fontsize=20)
plt.grid(True, linewidth=2, color="mistyrose")
plt.legend()
plt.show()
