import pandas as pd

Student_Name = 'Giovanni Andrés Acuña Morales'
ID_Student = 'A01794007'
print(f'Presentado por: {Student_Name}, con el código de Estudiante: {ID_Student}\n')

print(f'Module 4 - Model Development\n\n')

print(f'Question 1.\n')
print(f'Let X be a dataframe with 100 rows and 5 columns. Let y be the target with 100 samples. Assuming all the relevant libraries and data have been imported, the following line of code has been executed:\n\tLR = LinearRegression()\n\tLR.fit(X, y)\n\tyhat = LR.predict(X)\n\nHow many samples does yhat contain?')
print(f"\nThe answer is 100\n")

print(f'Question 2.\n')
print(f'What value of R^2 (coefficient of determination) indicates your model performs best?')
print(f"\nThe answer is 1\n")

print(f'Question 3.\n')
print(f'Which statement is true about polynomial linear regression?')
print(f"\nThe answer is\nAlthough the predictor variables of polynomial linear regression are not linear, the relationship between the parameters or coefficients is linear.")

print(f'Question 4.\n')
print(f'The larger the mean squared error, the better your model performs:')
print(f"\nThe answer is False\n")

print(f'Question 5.\n')
print(f"Assume all the libraries are imported. y is the target and X is the features or dependent variables. Consider the following lines of code:\n\n\tInput=[('scale',StandardScaler()),('model',LinearRegression())]\n\n\tpipe=Pipeline(Input)\n\n\tpipe.fit(X,y)\n\n\typipe=pipe.predict(X)\n\nWhat is the result of ypipe?")
print(f"\nThe answer is:\nStandardize the data, then perform prediction using a linear regression model.")