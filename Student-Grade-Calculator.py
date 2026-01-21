score = float(input("Enter your score between 0 and 100 : "))
if not 0<= score <= 100:
    grade = None
    print('Invalid score. Please enter a score between 0 and 100.')
elif 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    print('Invalid score. Please enter a score between 0 and 100.')
if grade is not None:
    print(f'yout grade is : {grade}')
