import random

characters = "ABCazDEybFcGHxdIweJvfKLugMNthOPsiQRjSrTkUVlWqXmYZn^op#&*_?/!@"
password_length = 8

def generate_password():
    password = ""
    for i in range(password_length):
        password+=random.choice(characters)
    return password

def write_to_file(name, site, password):
    format = f"{name} | {site} | {password}\n"
    with open("text.txt", "a") as f:
        f.write(format)

name = input("input your name: ")
site = input("website: ")
choice = input("would you like to generate a random password? (1 for yes): ")



#get the user input
#check if one of them is empty, notice them if so by a pop-up window
#format it
#append to the file
#check errors






if choice == "1":
    password = generate_password()
 
else:
   while True:
        password = input("input your password: ")
        if len(password) < password_length:
            print(f"password must be {password_length} characters long")
            continue
        break
  


write_to_file(name, site, password)



