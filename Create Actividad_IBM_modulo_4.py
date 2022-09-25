import pandas as pd

Student_Name = 'Giovanni Andrés Acuña Morales'
ID_Student = 'A01794007'
print(f'Presentado por: {Student_Name}, con el código de Estudiante: {ID_Student}\n')

print(f'Module 4 - Working with Data in Python \n\n')

print(f'Question 1.\n')
print(f'What do the following lines of code do?\n\n\twith open("Example1.txt","r") as file1:\n\t\tFileContent=file1.readlines()\n\t\tprint(FileContent)\n')

with open("Example1.txt","r") as file1:
    FileContent=file1.readlines()
    print(FileContent)

print(f'\nQuestion 2.\n')
print(f'What do the following lines of code do?\n\n\twith open("Example2.txt","w") as writefile:\n\t\twritefile.write("This is line A\ n")\n\t\twritefile.write("This is line B\ n")')

with open("Example2.txt","r") as file2:
    FileContent=file2.readlines()
    if len(FileContent) == 0:
        print(f'El archivo {file2.name} está vacio')
    else:
        print(FileContent)

with open("Example2.txt","w") as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

print(f'\nQuestion 3.\n')
print(f'What do the following lines of code do?\n\n\twith open("Example3.txt","a") as file1:\n\t\tfile1.write("This is line C\ n")')

with open("Example3.txt","r") as file3:
    FileContent=file3.readlines()
    if len(FileContent) == 0:
        print(f'El archivo {file3.name} está vacio')
    else:
        print(f'El archivo {file3.name} continue la data: {FileContent}')


with open("Example3.txt","a") as file3:
    file3.write("This is line C\n")

with open("Example3.txt","r") as file3:
    FileContent=file3.readlines()
    if len(FileContent) == 0:
        print(f'El archivo {file3.name} está vacio')
    else:
        print(f'El archivo {file3.name} continue la data: {FileContent}')

print(f'\nQuestion 4.\n')
print(f'What is the result of applying the following method df.head() to the dataframe "df"?')

df = pd.DataFrame({'animal':['snake', 'bat', 'tiger', 'lion','fox', 'eagle', 'shark', 'dog', 'deer']})
print(df)

print(df.head())