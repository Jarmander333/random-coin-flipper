import random

head = 0
tail = 0

flips = input("Please enter the amount of flips you'd like to execute: ")

for i in range(int(flips)):
	side = random.randint(0, 1)
	if side == 0:
		print("Heads!")
		head = head + 1
	else:
		print("Tails!")
		tail = tail + 1
print(str(head) + " Heads!")
print(str(tail) + " Tails!")
