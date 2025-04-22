import random
import time
import os

# Wait for (num) seconds while displaying the time left
def sleep(num):
    for x in range (num):
        print("\rTime left to memorize: {} seconds.".format(num - x-1), end=" ")
        time.sleep(1)

# Get the numbers of numbers + wait time
Guesser = []
ToBe = int(input("How many at once: "))
UserTime = int(input("How much time do you want: "))
while ToBe > 0:
    add = int(random.randrange(1, 9))
    Guesser.append(add)
    ToBe-=1

# Display the numbers
for x in Guesser:
    print(x, end=" ")
print("\n")

# Wait then clear
sleep(UserTime)
os.system('cls' if os.name == 'nt' else 'clear') 

# Input
user_input = input("Enter numbers (seperated by spaces): ")
user_guess = [int(num) for num in user_input.strip().split()]

# Checking
if user_guess == Guesser:
    print("good")
else:
    print("dumbass")
    print("correct answer was: ")
    for x in Guesser:
        print(x, end=" ")
