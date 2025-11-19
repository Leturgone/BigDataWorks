import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.formula.api import ols
from scipy import stats
import statsmodels.api as sm
from itertools import combinations

from statsmodels.sandbox.stats.multicomp import MultiComparison
from statsmodels.stats.anova import anova_lm

# Задание 3

data_path = 'insurance.csv'
df = pd.read_csv(data_path)

# Задание 3.1

groups = [df.loc[df["region"] == r, "bmi"].values for r in df["region"].unique()]
F, p = stats.f_oneway(*groups)
print(f"\n ANOVA (SciPy): F = {F:.4f}, p-value = {p:.6f}")

# Задание 3.2

print(f"\n ANOVA (statsmodels)")

# Строим модель линейной регрессии с фактором 'region' и зависимой переменной 'bmi'
model = ols('bmi ~ C(region)', data=df).fit()

# Выполняем ANOVA с помощью anova_lm()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

# Задание 3.3

regions = df["region"].unique()
alpha = 0.05
m = len(list(combinations(regions, 2)))
rows = []

for a, b in combinations(regions, 2):
    tstat, pval = stats.ttest_ind(
        df.loc[df["region"] == a, "bmi"],
        df.loc[df["region"] == b, "bmi"],
        equal_var=False
    )
    rows.append({ "Пары": f"{a}–{b}", "p_value": pval, "Решение": "отвергаем H₀" if pval < alpha/m else "оставляем H₀" })

t_df = pd.DataFrame(rows)

print("\n Парные t-тесты (с поправкой Бонферрони):\n", t_df)

# Задание 3.4

mc = MultiComparison(df["bmi"], df["region"])
tukey_test = mc.tukeyhsd(alpha=0.05)
print("Пост-хок тест Тьюки:\n", tukey_test.summary())
tukey_test.plot_simultaneous()
plt.title("Пост-хок тест Тьюки: BMI между регионами")
plt.tight_layout()
plt.show()


# Задание 3.5

model_two = ols("bmi ~ C(region) + C(sex) + C(region):C(sex)", data=df).fit()
anova_two = anova_lm(model_two, typ=2)
print("Двухфакторный ANOVA:\n", anova_two)


# Задание 3.6

df["region_sex"] = df["region"].astype(str) + "/" + df["sex"].astype(str)
mc2 = MultiComparison(df["bmi"], df["region_sex"])
tukey2 = mc2.tukeyhsd(alpha=0.05)
print("Пост-хок тест Тьюки между комбинациями region/sex:\n", tukey2.summary())
tukey2.plot_simultaneous()
plt.title("Пост-хок тест Тьюки: BMI между комбинациями region/sex")
plt.tight_layout()
plt.show()