import pandas as pd

Student_Name = 'Giovanni Andrés Acuña Morales'
ID_Student = 'A01794007'
print(f'Presentado por: {Student_Name}, con el código de Estudiante: {ID_Student}\n')

print(f'Module 3 - Exploratory Data Analysis\n\n')

print(f'Question 1.\n')
print(f'Consider the dataframe "df". What method provides the summary statistics?\n\n')

print(f"First we made the DataFrame with the column 'Fuel'\n With the command : df = pd.DataFrame(data = 'Fuel': [ 'gas', 'diesel', 'gas', 'diesel', 'gas', 'diesel', 'diesel', 'diesel', 'gas', 'gas'])\n")

df = pd.DataFrame(data = {'Fuel': [ 'gas', 'diesel', 'gas', 'diesel', 'gas', 'diesel', 'diesel', 'diesel', 'gas', 'gas']})

print(df)
print(f"\nAnd apply the command: df.describe()\nAnd the result is:\n")
print(df.describe())

print(f'\nQuestion 2.\n')
print(f"Consider the following dataframe:\n\n\tdf_test = df['body-style', 'price']\n\nThe following operation is applied:\n\n\tdf_grp = df_test.groupby(['body-style'], as_index=False).mean()\n\nWhat are resulting values of df_grp[‘price’]?")

print(f"First we made the DataFrame df\n With the command : df = pd.DataFrame(data = 'body-style': [ 'gas', 'diesel', 'gas', 'diesel', 'gas'], 'prices': [ '100', '200', '300', '400', '500'])\n")

df = pd.DataFrame(data = {'body-style': [ 'gas', 'diesel', 'gas', 'diesel', 'gas'], 'price': [ 100, 200, 300, 400, 500]})
print(df)

print(f"\nAnd apply the commands:\n\n\tdf_test = df['body-style', 'price']\n\n\tdf_grp = df_test.groupby(['body-style'], as_index=False).mean()\n\nAnd the result is:\n")

df_test = df[['body-style', 'price']]
df_grp = df_test.groupby(['body-style'], as_index=False).mean()
print(df_grp['price'])

print(f'\nQuestion 3.\n')
print(f'Correlation implies causation:\n')
print('The answer is False!')

print(f'\nQuestion 4.\n')
print(f"What is the minimum possible value of Pearson's Correlation?\n")
print('The answer is -1')

print(f'\nQuestion 5.\n')
print(f"What is the Pearson correlation between variables X and Y if X=Y:\n")
print('The answer is 1')