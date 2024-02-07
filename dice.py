import random

diceinput = input("Enter the number of dice to roll from [1-6]: ")

while not diceinput.isdigit() or not 1 <= int(diceinput) <= 6:
    print("Please enter a number from 1-6")
    diceinput = input("Enter the number of dice to roll from [1-6]: ")

for i in range(0, int(diceinput)):
    print(random.randint(1, 6))