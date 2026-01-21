numbers = [511, 260, 261, 912, 362, 473, 893, 277, 351, 494,
486, 885, 341, 484, 598, 950, 859, 716, 488, 584]
# sort the list
numbers.sort()
# loop through the list
for number in numbers:
    # check if the number is divisible by 9
    if number % 9 == 0:
        print(f"The smallest multiple of 9 is {number}")
        break