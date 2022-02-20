import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "@()[]{}"

all = lower + upper + numbers + symbol
length = 16
password = "".join(random.sample(all, length))
print(password)