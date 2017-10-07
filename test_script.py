
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from pandas import Series



df = pd.read_csv("PR-41713 product_attributes_train.csv", error_bad_lines=False,
                 names  = ['id', 'attribute_name',
                           'attribute_type',
                           'attribute_value'], sep = ";")
print()
print('/////////////')
#print(df)
#print(df[1:])

print(df[1:]['attribute_name'].value_counts())

print(df[1:]['attribute_value'].value_counts())


lst = df[1:]['attribute_name'].unique()
ss = {}

lst2 = df[1:][['attribute_name', 'id']]

print(lst2.sort_values(by='attribute_name'))

lst3 = {}
i=0
for x, y in zip(lst2["attribute_name"], lst2["id"]):
    #print(x)
    #print(y)

    if x == 'Страна производитель':
        lst3['Страна производитель'].add(y)

print(lst3)