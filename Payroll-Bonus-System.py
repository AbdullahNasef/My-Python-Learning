# getting the number of hours and rate 

num_hour = float(input('Enter the number of hours per month:'))
rate = float(input("Enter your hourly rate:"))
# The basic hours and bonus rate

base_hours = 100 
bonus = 2
# check if the number of hours is greater than the base hours 

if num_hour > base_hours:
    over_hours = num_hour - base_hours
    salary = (base_hours * rate) +(over_hours * rate * bonus)
else:
    salary = num_hour * rate

# print the salary 

print(f"you have worked {num_hour} hours this month,your salary is {salary:,.2f} $")
