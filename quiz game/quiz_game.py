print("Welcome to my game")


playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play: )")
score = 0

answer = input("What does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorect!")


answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else: 
    print("Incorect!")

print("You got " + str(score) + " question correct")
print("You got " + str((score/4) * 100) + "%")