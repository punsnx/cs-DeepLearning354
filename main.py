import pandas as pd

data = [[50, True], [40, False], [30, False]]

df = pd.DataFrame(data)

print(df.iloc[1, 0])
