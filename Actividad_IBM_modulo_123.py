Student_Name = 'Giovanni Andrés Acuña Morales'
ID_Student = 'A01794007'
print(f'Presentado por: {Student_Name}, con el código de Estudiante: {ID_Student}\n')


print(f'Module 1 - Python Basics\n\n')

print(f' Review Question 1.\n')
print(f'What is the result of the following operation in Python: 3 + 2 * 2\n')
print(3 + 2 * 2)

print(f'Review Question 2\n')
print(f"In Python, if you executed name = 'Lizz', what would be the output of print(name[0:2])?\n")
name = 'Lizz'
print(name[0:2])

print(f'Review Question 3\n')
print(f"In Python, if you executed var = '01234567', what would be the result of print(var[::2])?\n")
var = '01234567'
print(var[::2])

print(f'Review Question 4\n')
print(f"In Python, what is the result of the following operation '1'+'2'?\n")
print('1'+'2')

print(f'Review Question 5\n')
print(f"Given myvar = 'hello', how would you convert myvar into uppercase?\n")
myvar = 'hello'
print(myvar)
print(myvar.upper())

print(f'Module 2 - Python Data Structures\n\n')

print(f'Question 1\n')
print(f'What is the syntax used to obtain the first element of the tuple:\n')
A = ('a','b','c')
print(A)
print(A[0])

print(f'Question 2\n')
print(f"After applying the following method, L.append(['a','b']), the following list will only be one element longer.\n")
L = []
L.append(['a','b'])
print(L)

print(f'Question 4\n')
print(f'Consider the following Python dictionary:\n')
Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
print(f'What is the result of the following operation: Dict["D"]?\n')
Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
print(Dict)
print(Dict["D"])

print(f'Module 3 - Python Programming Fundamentals\n\n')

print(f'Question 1\n')
print(f'What is the output of the following lines of code:\n')
x=1
if(x!=1):
  print('Hello')
else:
  print('Hi')
print('Mike')

print(f'Question 2\n')
print(f'What is the output of the following few lines of code?\n')

A = ['1','2','3']
for a in A:
    print(2*a)
print(f"A = ['1','2','3']\n")
for a in A:
  print(2*a)

print(f'Question 3\n')
print(f'Consider the function Delta, when will the function return a value of 1\n')
def Delta(x):
  if x==0:
    y=1;
  else:
    y=0;
  return(y)
print(Delta(0))

print(f'Question 4\n')
print(f"What is the correct way to sort the list 'B' using a method? The result should not return a new list, just change the list 'B'.\n")
B = ['Ford', 'BMW', 'Volvo', 'Chevere', 'Bicicleta']
print(B)
B.sort()
print(B)

print(f'Question 5\n')
print(f"What are the keys of the following dictionary: 'a':1,'b':2?\n")
dict = {'a':1,'b':2}
print(dict)
print(dict.keys())
