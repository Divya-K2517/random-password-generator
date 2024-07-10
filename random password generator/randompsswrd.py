import random
import string

print("Welcome to the random password generator! First answer some questions about what type of password you want")

length = int(input("How many characters long do you want your password to be?(nonzero, positive, whole numbers only): " ))
num = input("Would you like numbers in your password? Enter y for yes and n for no: " )
punc = input("Would you like punctuation in your password? Enter y for yes and n for no: " )
upper = input("Would you like uppercase letters in your password? Enter y for yes and n for no: " )

char_lst = []
for x in string.ascii_lowercase:
    char_lst.append(x)
if upper == "y":
    for x in string.ascii_uppercase:
        char_lst.append(x)
if num == "y":
    for x in string.digits:
        char_lst.append(x)
if punc == "y":
    for x in string.punctuation:
        char_lst.append(x)
    
def gen_password(len):
    lst  = [] 
    password = ""
    for i in range(len):
        lst.append(random.choice(char_lst))
        
    for char in lst:
        password = password + char
    return password

print("Your password is: ", gen_password(length))

