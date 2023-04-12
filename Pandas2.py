import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

a=pd.DataFrame([[420, 380, 390],[50, 40, 45]],columns=['Pen','Shirt','Book'])

print(df)
print(a)