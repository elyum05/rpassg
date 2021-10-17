import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()

nums = "0123456789"
symbs = "!@#$%^&*()"

all = ""

length = int(input("Enter length: "))
amount = int(input("Enter amount: "))

q = input("Do you want to on uppercase letters: y/n: ")
q1 = input("Do you want to on lowercase letters: y/n: ")
q2 = input("Do you want to on numbers letters: y/n: ")
q3 = input("Do you want to on symbols letters: y/n: ")

if q == "y":
   uppers = True
elif q == "n":
   uppers = False
if q1 == "y":
   lowers = True
elif q1 == "n":
   lowers = False
if q2 == "y":
   numbers = True
elif q2 == "n":
   numbers = False
if q3 == "y":
   symbols = True
elif q3 == "n":
   symbols = False
else:
   print("Please, try again.")

if uppers:
   all += uppercase
if lowers:
   all += lowercase
if numbers:
   all += nums
if symbols:
   all += symbs

for x in range(amount):
   password = "".join(random.sample(all, length))
   print(password)