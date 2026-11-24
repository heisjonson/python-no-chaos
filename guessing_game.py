
random = 41

while True:
    number = int(input("Enter A Random Number (1-100): "))

    if number == -1:
        print("You quit the game")
        break

    if number < 1 or number > 100:
        print("Please enter a number between 1 and 100.")
        continue

    if number == random:
        print(f"You guessed right! The number is {random}")
        break

    print("Try again")


