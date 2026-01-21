name = input("whats your name?:")
age = input("how old are you?:")
is_student_input = input("Are you a student? (yes / no):")
is_student = True if is_student_input.lower() == "yes" else False
subjects = input("List the subjects you are studying (separate with commas):")
print("hello" , name)
print("Age:" , age)
print("is a student?:", is_student)
