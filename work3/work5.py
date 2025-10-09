import pandas as pd
from scipy.stats import chi2_contingency

# Задание 15

data = pd.DataFrame({
    'Женат': [89, 17, 11, 43, 22, 1],
    'Гражданский брак': [80, 22, 20, 35, 6, 4],
    'Не состоит в отношениях': [35, 44, 35, 6, 8, 22]
})
data.index = ['Полный рабочий день', 'Частичная занятость', 'Временно не работает',
              'На домохозяйстве', 'На пенсии', 'Учёба'
              ]
hi2, p, dof, expected = chi2_contingency(data)

print("χ2 =", hi2)
print("p-value =", p)
print("Степени свободы =", dof)
print("Ожидаемые частоты:\n", expected)
