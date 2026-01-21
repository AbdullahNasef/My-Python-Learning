user =  "mohamed_g@codeea.com"
password = 'p@ssw0rd123'

input_user = input("Enter your email: ")
input_password = input("Enter your password: ")

if input_user == user and input_password == password:
    print("Login successful!")
else:
    print("Invalid email or password.")
