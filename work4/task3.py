import pandas as pd
from statsmodels.formula.api import ols
from scipy import stats
import statsmodels.api as sm

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

