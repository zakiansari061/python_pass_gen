import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "{}[]()@;:*^_!%^&"
number = "123456789"
all = lower + upper + symbols + number

length = 16

password = "".join(random.sample(all, length))

print(password)
