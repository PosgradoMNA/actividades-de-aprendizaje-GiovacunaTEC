Student_Name = 'Giovanni Andrés Acuña Morales'
ID_Student = 'A01794007'
print(f'Presentado por: {Student_Name}, con el código de Estudiante: {ID_Student}')


# Module 1 - Python Basics

## Review Question 1.

#What is the result of the following operation in Python: 3 + 2 * 2
print(3 + 2 * 2)


##Review Question 2

#In Python, if you executed name = 'Lizz', what would be the output of print(name[0:2])?
name = 'Lizz'
print(name[0:2])


##Review Question 3

#In Python, if you executed var = '01234567', what would be the result of print(var[::2])?
var = '01234567'
print(var[::2])


##Review Question 4

#In Python, what is the result of the following operation '1'+'2'?
print('1'+'2')


##Review Question 5

#Given myvar = 'hello', how would you convert myvar into uppercase?
myvar = 'hello'
print(myvar)
print(myvar.upper())



#Module 2 - Python Data Structures

##Question 1

#What is the syntax used to obtain the first element of the tuple:
A = ('a','b','c')
print(A)
print(A[0])


##Question 2

#After applying the following method, L.append(['a','b']), the following list will only be one element longer.
L = []
L.append(['a','b'])
print(L)


##Question 4

#Consider the following Python dictionary:

Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}

#What is the result of the following operation: Dict["D"]?
Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}
print(Dict)
print(Dict["D"])



#Module 3 - Python Programming Fundamentals

##Question 1

#What is the output of the following lines of code:

x=1

if(x!=1):

  print('Hello')

else:

  print('Hi')

print('Mike')

##Question 2

#What is the output of the following few lines of code?

A = ['1','2','3']

for a in A:

    print(2*a)

#A = ['1','2','3']

for a in A:

  print(2*a)


##Question 3

#Consider the function Delta, when will the function return a value of 1

def Delta(x):

  if x==0:

    y=1;

  else:

    y=0;

  return(y)

print(Delta(0))


##Question 4

#What is the correct way to sort the list 'B' using a method? The result should not return a new list, just change the list 'B'.
B = ['Ford', 'BMW', 'Volvo', 'Chevere', 'Bicicleta']
print(B)
B.sort()
print(B)


##Question 5

#What are the keys of the following dictionary: {'a':1,'b':2}?
dict = {'a':1,'b':2}
print(dict)
print(dict.keys())
