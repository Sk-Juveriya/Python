import pandas as pd
data={

    "Name":["Alice","Bob","Charlie","David"],
    "Age":[25,30,45,67],
    "City":['New York','Los Angeles','Chicago','Houstan']

}
df=pd.DataFrame(data)
print("Data:")
print(df)
print("\nDataFrame Information:")
print(df.info())

Series=pd.Series(data)
print("\nSeries:")
print(Series)



    #OUTPUT
# Data:
#       Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   45      Chicago
# 3    David   67      Houstan

# DataFrame Information:
# <class 'pandas.DataFrame'>
# RangeIndex: 4 entries, 0 to 3
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Name    4 non-null      str
#  1   Age     4 non-null      int64
#  2   City    4 non-null      str
# dtypes: int64(1), str(2)
# memory usage: 228.0 bytes
# None

# Series:
# Name                 [Alice, Bob, Charlie, David]
# Age                              [25, 30, 45, 67]
# City    [New York, Los Angeles, Chicago, Houstan]
# dtype: object
