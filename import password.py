

import string
import random


length=int(input("enter password length:"))

print('''choose character set for password from these:
      1.digits
      2.letters
      3.special characters
      4.exit''')

characterlist=""

while(True):
    choice=int(input("pick a number"))
    if(choice==1):
        characterlist +=string.ascii_letters
    elif(choice==2):
        characterlist +=string.digits  
    elif(choice==3):
        characterlist +=string.punctuation  
    elif(choice==4):
        break
    else:
        print("please pick a valid option!")

    password=[]

    for i in range(length):

        randomchar=random.choice(characterlist)

        password.append(randomchar)

    print("the random password is"+"".join(password))
