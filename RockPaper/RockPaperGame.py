# Write your code here
import random

outcome = ["rock", "paper", "scissors"]
name = str(input("Enter your name: "))
print("Hello,", name)
fl = open('rating.txt', 'r')
score = 0
if fl.mode == 'r':
    content = fl.readlines()
    for x in content:
        if name in x:
            y = x.split(" ")
            score += int(y[1])
            print("> !rating")
            print("Your rating:", int(y[1]))
            break
choice = str(input())
if choice != "":
    outcome = choice.split(",")

length = len(outcome)
print("Okay, let's start")
itr = True
while (itr):
    comp = random.randint(0, length - 1)
    flag = False
    index = 0
    val = input()
    result = []
    for value in outcome:
        if value == val:
            flag = True
            continue
        else:
            index += 1
        if flag:
            result.append(value)
            index -= 1
    for i in range(0, index):
        result.append(outcome[i])

    if val == outcome[comp]:
        print("There is a draw ", outcome[comp])
        score += 50
    elif (val in outcome) and (val != outcome[comp]):
        tmpIndex = result.index(outcome[comp])

        if tmpIndex < len(result) / 2:
            print("Sorry, but the computer chose ", result[tmpIndex])
        elif tmpIndex >= len(result) / 2:
            print("Well done. The computer chose ", result[tmpIndex], " and failed")
            score += 100
    elif val == "!rating":
        print("Your rating: ", score)
    elif val == "!exit":
        print("Bye!")
        break
    else:
        print("Invalid input")
    fl.close()
