# get the full name
name = input("Enter your full name: ")

# get the index of the first space
space_index = name.index(" ")

# get the first name
n_name= name[:space_index]
# greet the user
print(f"Hello,{n_name.title()}!\nWelcome at Codezilla!")