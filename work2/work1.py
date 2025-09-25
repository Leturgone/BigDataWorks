import pandas as pd
import plotly.graph_objs as go

# Задание 1

# Загрузка данных
data_path = 'games.csv'
df = pd.read_csv(data_path)

# Задание 2
# Общая информация
print("Информация о данных:")
print(df.info())

print("\nПервые строки данных:")
print(df.head())

# Проверка пропусков
print("\nПроверка на пропущенные значения:")
print(df.isnull().sum())

# Удаление пустых строк
df.dropna(subset=['Rating', 'Summary', 'Team'], inplace=True)
print("\nПосле удаления:")
print(df.isnull().sum())

# Задание 3


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


x_data = df['Title'].loc[0:250]
y_data = df['Plays'].loc[0:250].apply(convert_players)
color_data = df['Rating'].loc[0:250].astype(float)

# Бар-чарт
fig = go.Figure(data=[go.Bar(
    x=x_data,
    y=y_data,
    marker=dict(
        color=color_data,
        coloraxis="coloraxis",
        line=dict(color='black', width=2)  # границы столбцов
    )
)])

# Макет
fig.update_layout(
    title={
        'text': "Игры, рейтинг и количество игроков",
        'x': 0.5,  # по центру
        'xanchor': 'center',
        'y': 0.95,
        'yanchor': 'top',
        'font': dict(size=20)
    },
    xaxis=dict(
        title=dict(text="Название игры", font=dict(size=16)),
        tickangle=315,
        tickfont=dict(size=14),
        showgrid=True,
        gridwidth=2,
        gridcolor="ivory"
    ),
    yaxis=dict(
        title=dict(text="Количество игроков", font=dict(size=16)),
        tickfont=dict(size=14),
        showgrid=True,
        gridwidth=2,
        gridcolor="ivory"
    ),
    width=None,  # во всю ширину
    height=700,
    margin=dict(l=0, r=0, t=50, b=0),  # убираем лишние отступы
    coloraxis=dict(
        colorscale='Viridis',
        colorbar=dict(title='Рейтинг')
    ),
    plot_bgcolor='white'
)

# Вывод графика
fig.show()
