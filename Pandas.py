import pandas as pd
pricelist=[100, 200, 300, 400]


productseries=pd.Series(pricelist,index=['Pen','Shirt','Book','Mouse'])
print(productseries)