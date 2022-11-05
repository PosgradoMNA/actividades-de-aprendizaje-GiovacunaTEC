import pandas as pd

Student_Name = 'Giovanni Andrés Acuña Morales'
ID_Student = 'A01794007'
print(f'Presentado por: {Student_Name}, con el código de Estudiante: {ID_Student}\n')

print(f'Module 5 – Model Evaluation\n\n')

print(f'Question 1.\n')
print(f'In the following plot, the vertical axis shows the mean square error and the horizontal axis represents the order of the polynomial. The red line represents the training error the blue line is the test error. What is the best order of the polynomial given the possible choices in the horizontal axis?')
print(f"\nThe answer is 8\n")

print(f'Question 2.\n')
print(f'What is the correct use of the "train_test_split" function such that 40% of the data samples will be utilized for testing; the parameter "random_state" is set to zero; and the input variables for the features and targets are_data, y_data respectively?')
print(f"\nThe answer is\ntrain_test_split(x_data, y_data, test_size=0.4, random_state=0)\n")

print(f'Question 3.\n')
print(f'What is the output of cross_val_score(lre, x_data, y_data, cv=2)?')
print(f"\nThe average R^2 on the test data for each of the two folds.\n")

print(f'Question 4.\n')
print(f'What is the code to create a ridge regression object "RR" with an alpha term equal 10?')
print(f"\nThe answer is RR=Ridge(alpha=10)\n")

print(f'Question 5.\n')
print(f"What dictionary value would we use to perform a grid search for the following values of alpha: 1,10, 100? No other parameter values should be tested.\n")
print(f"The answer is\n")
print("[{'alpha': [1,10,100]}]")