import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading json file
json_data = pd.read_json('data.json')
#print(json_data)


#Reading csv file
csv_data = pd.read_csv('data.csv')
pd.options.display.max_rows = 9999
#print(csv_data)
#print(csv_data.head(20))
#print(csv_data.tail(20))
print(csv_data.info())
new_df = csv_data.dropna()
#print(new_df.to_string())

df = pd.read_csv('data.csv')
df.dropna(inplace = True)
#print(df.to_string())

df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)
#print(df.to_string())

df = pd.read_csv('data.csv')
x = df['Calories'].mean()
df.fillna(x, inplace = True)
#print(df.head(20))

df = pd.read_csv('data.csv')
x = df["Calories"].median()
df.fillna(x, inplace = True)
#print(df.head(20))

df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0]
df.fillna(x, inplace = True)
#print(df.head(30))

df = pd.read_csv('data.csv')
print('df : ',df.corr())

df.plot()
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()


