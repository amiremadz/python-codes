import pandas as pd

data_1 = {'id': ['1', '2', '3', '4'],
          'name': ['al' , 'mike', 'jack', 'peter']}
df_1   = pd.DataFrame(data_1, columns=['id', 'name'])

data_2 = {'gender': ['f', 'm', 'm', 'm']}
df_2   = pd.DataFrame(data_2, columns=['gender'], index=['al', 'mike', 'jack', 'peter'])

data_3 = {'gender': ['f', 'm', 'm']}
df_3   = pd.DataFrame(data_3, columns=['gender'], index=['al', 'mike', 'jack'])

data_4 = {'gender': ['m', 'f', 'm']}
df_4   = pd.DataFrame(data_4, columns=['gender'], index=['mike', 'al', 'jack'])

data_5 = {'gender': ['m', 'm', 'm']}
df_5   = pd.DataFrame(data_4, columns=['gender'], index=['mike', 'george', 'jack'])

print('df1:')
print(df_1)

print('\ndf2:')
print(df_2)

print('\ndf3:')
print(df_3)

print('\ndf4:')
print(df_4)

print('\ndf5:')
print(df_5)

print('\nmerge df1 and df2:')
dfm_12 = pd.merge(df_1, df_2, left_on='name', right_index=True)
print(dfm_12)


print('\nmerge df1 and df3:')
dfm_13 = pd.merge(df_1, df_3, left_on='name', right_index=True)
print(dfm_13)

print('\nmerge df1 and df4:')
dfm_14 = pd.merge(df_1, df_4, left_on='name', right_index=True)
print(dfm_14)

print('\nmerge df1 and df5:')
dfm_15 = pd.merge(df_1, df_5, left_on='name', right_index=True, how='inner')
print(dfm_15)

print('\nmerge df1 and df5:')
dfm_15 = pd.merge(df_1, df_5, left_on='name', right_index=True, how='outer')
print(dfm_15)
