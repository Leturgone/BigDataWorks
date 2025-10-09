import numpy as np
from scipy import stats

# Задание 14

observed = np.array([97, 98, 109, 95, 97, 104])

expected = np.array([100, 100, 100, 100, 100, 100])

chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)

print("Статистика χ2 =", chi2_stat)
print("p-value =", p_value)
