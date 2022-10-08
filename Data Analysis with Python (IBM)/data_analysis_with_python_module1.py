import pandas as pd

Student_Name = 'Giovanni Andrés Acuña Morales'
ID_Student = 'A01794007'
print(f'Presentado por: {Student_Name}, con el código de Estudiante: {ID_Student}\n')

print(f'Module 1 - Introduction\n\n')

print(f'Question 1.\n')
print(f'What does CSV stand for?\n\n')

print(f'Comma-separated values\n\n')

print(f'Question 2.\n')
print(f'In the data set, which of the following represents an attribute or feature?\n\n')

print(f'Column\n\n')

print(f'Question 3.\n')
print(f'What is the name of what we want to predict?\n\n')

print(f'Target\n\n')

print(f'Question 4.\n')
print(f'What is the command to display the first five rows of a dataframe df?\n\n')

print(f'Este es un dataframe con el nombre: spanishPlayersDF\n\n')

print(f'df.head()\n\n')

spanishPlayersDF = pd.DataFrame(
    {
        'name': ['Casillas', 'Ramos', 'Pique', 'Puyol', 'Capdevila', 'Xabi Alonso', 'Busquets', 'Xavi Hernandez',
                 'Pedrito', 'Iniesta', 'Villa'],
        'demarcation': ['Goalkeeper', 'Right back', 'Centre-back', 'Centre-back', 'Left back', 'Defensive midfield',
                        'Defensive midfield', 'Midfielder', 'Left winger', 'Right winger', 'Centre forward'],
        'team': ['Real Madrid', 'Real Madrid', 'FC Barcelona', 'FC Barcelona', 'Villareal', 'Real Madrid',
                 'FC Barcelona', 'FC Barcelona', 'FC Barcelona', 'FC Barcelona', 'FC Barcelona']
    }, columns=['name', 'demarcation', 'team'], index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
)
print(spanishPlayersDF)

print(f'Al aplicar la función df.head() obtenemos\n\n')

print(spanishPlayersDF.head())

print(f'Question 5.\n')
print(f'What command do you use to get the data type of each row of the dataframe df?\n\n')

print(f'df.dtypes()\n\n')

print(f'Usando el mismo dataframe spanishPlayersDF se usará la función df.dtypes\n\n')

print(spanishPlayersDF.dtypes)

print(f'Question 6.\n')
print(f'How do you get a statistical summary of a dataframe df?\n\n')

print(f'df.describe()\n\n')

print(f'Usando el mismo dataframe spanishPlayersDF se usará la función df.dtypes\n\n')

print(spanishPlayersDF.describe())

print(f'Question 7.\n')
print(f'If you use the method describe() without changing any of the arguments, you will get a statistical summary of all the columns of type "object".\n\n')

print(f'False\n\n')

print(f'Thanks\n\n')
