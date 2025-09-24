from sklearn.datasets import fetch_california_housing
import pandas as pd

data = fetch_california_housing(as_frame=True)

df = pd.DataFrame(data.data, columns=data.feature_names)

filtered_df = df.loc[(df['HouseAge'] > 50) & (df['Population'] > 2500)]
print("средний возраст домов в районе более 50 лет инаселение более 2500 человек:")
print(filtered_df)
