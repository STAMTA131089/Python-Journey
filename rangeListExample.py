#Random password generator
import random
charlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specialcharlist = ['.',',','?','_','(',')']
number = [0,1,2,3,4,5,6,7,8,9]
all = [charlist,specialcharlist,number]
Pwd_length = int(input("How many letters you need in password? \n"))
num = int(input("How many numbers you need in password? \n"))
sp = int(input("How many  char you need in password? \n"))

# if num + sp > Pwd_length:
#     print("invalid password inputs provided.")
# else:
password = ""
for i in range(1,Pwd_length+1):
    if i == 1:
        for j in range(num):
            password += str(random.choice(number))
    elif i==2:
        for k in range(sp):
            password += str(random.choice(specialcharlist))    
    else:
        password += random.choice(charlist)
print(password)
    




