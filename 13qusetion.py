

import pandas as pd

data1 = {'A': [1, 2, 3],
         'B': [4, 5, 6]}
data2 = {'A': [7, 8, 9],
         'B': [10, 11, 12]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

concatenated_df = pd.concat([df1, df2])

print("Concatenated DataFrame:")
print(concatenated_df)

