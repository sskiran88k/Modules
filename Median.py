import pandas as pd

a=[[1, 2, 3, 6],[4, 5, 6, 8],[6, 7, 8, 9],[1, 2, 4, 6],[6, 7, 8, 2], [4, 3, 7, 9]]
b=pd.DataFrame(a)
print(b)
print(b.median())
print(b.mean())

c=[[1, 2, 1, 5],[3, 4, 1, 1],[2, 2, 1, 5],[1, 1, 1, 2]]
d=pd.DataFrame(c)
print(d)
print(d.mean())
print(d.median())
print(d.mode())