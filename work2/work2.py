import pandas as pd
import plotly.graph_objs as go

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


# Задание 4

x_data = df['Title']
y_data = df['Plays'].apply(convert_players)

df_games = pd.DataFrame({
    'Title': x_data,
    'Plays': y_data
})

# Группируем по названию игры и суммируем количество игроков
grouped = df_games.groupby('Title', as_index=False).agg({'Plays': 'sum'})

# Сортируем по количеству игроков
top_games = grouped.sort_values(by='Plays', ascending=False).head(10)

labels = top_games['Title'].tolist()
values = top_games['Plays'].tolist()

# Строим круговую диаграмму с уникальными играми
fig = go.Figure(data=[go.Pie(
    labels=labels,
    values=values,
    marker=dict(
        line=dict(color='black', width=2)  # границы долей
    ),
    textinfo='label+percent+value',
    insidetextorientation='radial'
)])


fig.update_layout(
    title=dict(
        text='Топ-10 игр по количеству игроков',
        x=0.5,
        xanchor="center",
        font=dict(size=20)
    ),
    width=None,
    height=700,
    margin=dict(l=0, r=0, t=50, b=0),
)
fig.show()