import random

def generate_password(length):
  #generate a random password
  password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
  result_str = "";
  for i in range(length):
    index = random.randrange(len(password_chars))
    result_str += password_chars[index]
  return result_str

#get user input
length = int(input("How many characters do you want in your password? "))

#generate the password
password = generate_password(length)

#output the password to a file
file = open("password.txt", "a")
file.write(password)
file.write("\n")
file.close()

#output the password to the screen
print("Your new password is {}".format(password))