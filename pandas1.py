#### Series ####
import pandas as pd

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
