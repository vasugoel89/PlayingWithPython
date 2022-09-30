import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "123456789"
symbols = "!@#$%^&*/"
all = lower + upper + number + symbols 
length = 8

password = "".join(random.sample(all,length))
print(password)