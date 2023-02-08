import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''#### Series ####

a = [1,2,3,4]

op = pd.Series(a, index=['a','b','c','d'])
#print(op)
#print(op[1])
#print(op['a'])

# dict to series
calories = {"day1": 420, "day2": 380, "day3": 390}
cal_op = pd.Series(calories)
print(cal_op)

#DataFrame to Series
data = {
  "calories": [420, 480, 490],
  "duration": [50, 40, 45]
}

call_op = pd.Series(data['calories'], index=data['duration'])
print(call_op)

cal_dataframe = pd.DataFrame(data)
print(cal_dataframe.loc[0])

cal_dataframe_index = pd.DataFrame(data, index=['a','b','c'])
print(cal_dataframe_index.loc['b'])'''

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


