import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, np.nan]
})

df['Age'] = df['Age'].fillna(df['Age'].mean())

print(df)
