from sklearn.datasets import fetch_california_housing
import pandas as pd

data = fetch_california_housing(as_frame=True)

df = pd.DataFrame(data.data, columns=data.feature_names)

print("\nСредние значения признаков:")


def feature_mid(x):
    return x.mean()


mids = df.apply(feature_mid)
for feature, mean_value in mids.items():
    print(f"{feature}: {mean_value}")
