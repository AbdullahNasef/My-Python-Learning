# Initialize the list to store the numbers
numbers = []
num = 452

# Use a while loop to iterate through the range of numbers
while num < 983:
    if num % 5 == 0 and num % 7 == 0:
        numbers.append(num)
    # ملاحظة: سطر زيادة الرقم يجب أن يكون داخل الـ while وليس داخل الـ if
    num += 1

# Sort the list of numbers
numbers.sort()

# Get the second highest and second lowest numbers
# تأكد دائماً أن القائمة تحتوي على عناصر كافية لتجنب IndexError
second_highest = numbers[-2]
second_lowest = numbers[1]

# Calculate the average
average = (second_highest + second_lowest) / 2

# Print the result
print(f"The average of the second highest ({second_highest}) and "
      f"second lowest ({second_lowest}) numbers is: {average}")