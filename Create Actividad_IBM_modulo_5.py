import pandas as pd
import numpy as np

Student_Name = 'Giovanni Andrés Acuña Morales'
ID_Student = 'A01794007'
print(f'Presentado por: {Student_Name}, con el código de Estudiante: {ID_Student}\n')

print(f'Module 5 - Working with Numpy Arrays & Simple APIs\n\n')

print(f'Question 1.\n')
print(f'What is the result of the following lines of code:\n\n\ta=np.array([0,1,0,1,0])\n\tb=np.array([1,0,1,0,1])\n\ta*b\n')

a=np.array([0,1,0,1,0])
b=np.array([1,0,1,0,1])
print(a*b)

print(f'\nQuestion 2.\n')
print(f'What is the result of the following lines of code:\n\n\ta=np.array([0,1])\n\tb=np.array([1,0])\n\tnp.dot(a,b)\n')

a=np.array([0,1])
b=np.array([1,0])
print(np.dot(a,b))

print(f'\nQuestion 3.\n')
print(f'What is the result of the following lines of code:\n\n\ta=np.array([1,1,1,1,1])\n\ta+10\n')

a=np.array([1,1,1,1,1])
print(a+10)

print(f'\nQuestion 4.\n')
print(f'What is the correct code to perform matrix multiplication on the matrix A and B?\n')

print('np.dot(A,B)')