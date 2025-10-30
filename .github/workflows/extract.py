print("Extrct data from mysql")
import pandas as pd
data = {
    "id":[1,2,3],
    "name":["A","B","C"],
    "Age": [10,20,30]
}

df = pd.DataFrame(data)
print(df)