print("Welcome to my computer Quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okey! Let's play :) ")

answer = input("What does CPU stand for? ").lower()
score = 0
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What dose GPU stand for ").lower()
if answer == "graphical processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print("correct!")
    score += 1
else:
    print("Incorrect!")

print("you got " + str(score) + " questions correct..!")
print("you got " + str((score/4)*100) + "%.")