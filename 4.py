 Write a program to sort comma separated file.
  
import pandas as pd
data=pd.read_csv("sample.csv")
data.sort_values(["column1", "column2"])
print(data)
