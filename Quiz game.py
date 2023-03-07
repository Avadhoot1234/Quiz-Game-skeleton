print("Welcome to my Quiz Game")

playing=input("Do you want to play ")

if playing.lower()!="yes":
    quit()
print("Okay that's great let's start")
score=0

answer=input("What does the CPU stands for? ")
if answer.lower()=="central processing unit":
    print('The answer is correct!')
    score += 1
else:
    print("Sorry the answer is incorrect!")

answer=input("What does the GPU stands for? ")
if answer.lower()=="graphic processing unit":
    print("The answer is correct!")
    score += 1
else:
    print("Sorry the answer is incorrect!")

answer=input("What does the RAM stands for? ")
if answer.lower()=="random access memory":
    print("The answer is correct!")
    score += 1
else:
    print("Sorry the answer is incorrect!")

answer=input("What does the PSU stands for? ")
if answer.lower()=="power supply":
    print("The answer is correct!")
    score += 1
else:
    print("Sorry the answer is incorrect!")

answer=input("What does the SQL stands for? ")
if answer.lower()=="sequential query language":
    print("The answer is correct!")
    score += 1
else:
    print("Sorry the answer is incorrect!")

print("Your final score  is ",score)