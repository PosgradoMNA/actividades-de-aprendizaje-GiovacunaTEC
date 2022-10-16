import pandas as pd

Student_Name = 'Giovanni Andrés Acuña Morales'
ID_Student = 'A01794007'
print(f'Presentado por: {Student_Name}, con el código de Estudiante: {ID_Student}\n')

print(f'Module 2 - Data Wrangling\n\n')

print(f'Question 1.\n')
print(f"Consider the dataframe df. What is the result of the following operation: df['symbolling'] = df['symbolling'] + 1?\n\n")

print(f"First we made the DataFrame with the column 'symbolling'\n With the command : df = pd.DataFrame(columns = ['symbolling'])\n")
df = pd.DataFrame(data = {'symbolling': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]})

print(df)
print(f"\nAnd apply the command: df['symbolling'] = df['symbolling'] + 1\nAnd the result is:\n")
df['symbolling'] = df['symbolling'] + 1
print(df)

print(f'Question 2.\n')
print(f"Consider the dataframe df. What does the command df.rename(columns='a':'b') change about the dataframe df?\n\n")

print(f"First we made the DataFrame with two columns 'symbolling'\n With the command : df = pd.DataFrame(columns = ['First_Column', 'Second_Column'])\n")

df = pd.DataFrame(columns = ['First_Column', 'Second_Column'])
print(df.columns)
print(f"\nAnd apply the command: df.rename(columns='a':'b')\nAnd don't see the changes\n")

df.rename(columns={'a':'b'})
print(df.columns)

print(f'Question 3.\n')
print(f"Consider the dataframe df. What is the result of the following operation df['price'] = df['price'].astype(int)?\n\n")

print(f"First we made the DataFrame with the column price\n With the command : df = pd.DataFrame(columns = ['price'])\n")

df = pd.DataFrame(columns = ['price'])
print(df.info())
print(f"\nWe check the column type and see the column is the object type\n")
print(f"\nAnd apply the command: df['price'] = df['price'].astype(int)\nAnd we see the changes\n")

df['price'] = df['price'].astype(int)
print(df.info())


print(f'Question 4.\n')
print(f"Consider the column of the dataframe df['a']. The column has been standardized. What is the standard deviation of the values as a result of applying the following operation: df['a'].std()?\n\n")

print(f"First we made the DataFrame with the column 'a'\n With the command : df = pd.DataFrame(data = 'a': [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])\n")

df = pd.DataFrame(data = {'a': [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
print(df['a'])
print(f"\nAnd apply the command: df['a'].std()\nAnd we see the changes\n")
df['a'].std()
print(df['a'])

print(f'Question 5A.\n')
print(f"Consider the column of the dataframe, df['Fuel'], with two values: 'gas' and' diesel'. What will be the name of the new columns pd.get_dumies(df['Fuel']) ?\n\n")

print(f"First we made the DataFrame with the column 'Fuel'\n With the command : df = pd.DataFrame(data = 'Fuel': [ 'gas', 'diesel', 'gas', 'diesel', 'gas', 'diesel', 'diesel', 'diesel', 'gas', 'gas'])\n")

df = pd.DataFrame(data = {'Fuel': [ 'gas', 'diesel', 'gas', 'diesel', 'gas', 'diesel', 'diesel', 'diesel', 'gas', 'gas']})
print(df)

print(f"\nAnd apply the command: pd.get_dumies(df['Fuel']) \nAnd we see the changes\n")

print(pd.get_dummies(df['Fuel']))

print(f'\nQuestion 5B.\n')
print(f'What are the values of the new columns from part 5a)?\n\n')

print(pd.get_dummies(df['Fuel']))

print(f'\nThanks\n\n')