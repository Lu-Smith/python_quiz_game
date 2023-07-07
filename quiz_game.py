print("Welcome to my computer quiz")

playing = input("Do you want to play? (yes/no) ")

if playing != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("What does CPU stand for? ")

if answer.upper() == "CENTRAL PROCESSING UNIT":
    print("Correct!")