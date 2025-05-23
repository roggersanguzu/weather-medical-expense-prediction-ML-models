import pandas as pd 
"""
#Here mainly Raw Data
file = open('california_housing_test.csv')
content = file.read()
file.close()
print(content)
"""

#Here mainly Data Fram structure
content=pd.read_csv('california_housing_test.csv')
print(content)
print(content.head)
print(content['total_bedrooms'].sum())

