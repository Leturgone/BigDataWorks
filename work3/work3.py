import pandas as pd
from scipy import stats

# Задание 13

df = pd.read_csv("bmi.csv")

northwest_bmi = df[df["region"] == "northwest"]["bmi"]
southwest_bmi = df[df["region"] == "southwest"]["bmi"]

shapiro_northwest = stats.shapiro(northwest_bmi)
shapiro_southwest = stats.shapiro(southwest_bmi)

print("\nШапиро-Уилка для northwest:", shapiro_northwest)
print("\nШапиро-Уилка для southwest:", shapiro_southwest)

bartlett_test = stats.bartlett(northwest_bmi, southwest_bmi)
print("\nКритерий Бартлетта:", bartlett_test)

t_st_test = stats.ttest_ind(northwest_bmi, southwest_bmi, equal_var=True)
print("\nt-критерий Стьюдента:", t_st_test)
