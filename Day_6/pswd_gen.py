#Password Generator

import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
symbols=['!', '#', '$', '%', '&','?', '@','(',')']
print('Welcome to the Password Generator')
nr_letters=int(input('How many letters you want in your password?'))
nr_numbers=int(input('How many numbers so you want in your Password?'))
nr_symbols=int(input('How many special characters you want in your Password?'))

#Silly way 

# pwd_letters=random.sample(letters, nr_letters)
# pwd_numbers=random.sample(numbers, nr_numbers)
# pwd_symbols=random.sample(symbols,nr_symbols)

# password_list = pwd_letters + pwd_numbers + pwd_symbols
# #random.shuffle(password_list)
# password = "" .join(password_list)

# print(f'Your Password is  {password}')


#Smart and Hard way 

passwordl=[]
for char in range(0, nr_letters):
    passwordl.append(random.choice(letters))

for char in range(0, nr_numbers):
    passwordl.append(random.choice(numbers))

for char in range(0, nr_symbols):
    passwordl.append(random.choice(symbols))

print(passwordl)
random.shuffle(passwordl)

password=""
for char in passwordl:
    password+=char

print(f' Your Password is: {password}')