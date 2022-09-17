import pandas as pd 
 
df = pd.read_csv('GoogleApps.csv')
a = df[df['Type'] == 'Free']['Reviews'].max()
b = df[df['Type'] == 'Paid']['Reviews'].max()
print(a-b)