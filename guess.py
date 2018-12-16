questions = {
    1: "It is an animal",
    2: "It has 4 legs",
    3: "It has two horns",
    4: "It eats grass",
    5: "It gives milk",
}

def hint(choice):
    if (choice < 6) :
        print("Hint: " + questions[choice])

word = "Cow"
guess = ""
choice = 1
is_won = False

print("\n*** Welcome to Our Guess Game ***\n")

while choice < 6:
    guess = input("Guess the word: ")
    if guess.lower() == word.lower():
        is_won = True
        break
    hint(choice)
    choice += 1

if is_won:
    print("\nCongratulations, you won the game")
    if (choice == 1):
        print("You scored * * * * * stars")
    elif (choice == 2):
        print("You scored * * * *  stars")
    elif (choice == 3):
        print("You scored * * *  stars")
    elif (choice == 4):
        print("You scored * *   stars")
    else:
        print("You scored * star")
else:
    print("\nSorry, you lose the game, better luck next time")
