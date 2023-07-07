print("Welcome to my computer quiz")

playing = input("Do you want to play? (yes/no) ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer0 = input("What does CPU stand for? ")

if answer0.upper() == "CENTRAL PROCESSING UNIT":
    print("Correct!")
else:
    print("Incorrect!")

answer1 = input("What does GPU stand for? ")

if answer1.upper() == "GRAPHICS PROCESSING UNIT":
    print("Correct!")
else:
    print("Incorrect!")

answer2 = input("What does RAM stand for? ")

if answer2.upper() == "RANDOM ACCESS MEMORY":
    print("Correct!")
else:
    print("Incorrect!")

answer3 = input("What does PSU stand for? ")

if answer3.upper() == "POWER SUPPLY UNIT":
    print("Correct!")
else:
    print("Incorrect!")
