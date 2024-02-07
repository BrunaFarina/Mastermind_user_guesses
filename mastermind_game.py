import random

board = ["_", "_", "_", "_"]

def input_number():
    number = random.randint(1000, 9999)
    return number

def mastermind():
    random_number = str(input_number())
    lives = 10
    board_check = ""

    while board_check != random_number and lives > 0:
        print('You have', lives, "lives left")
        print(board[0] + board[1] + board[2] + board[3])
        guess = input("Guess a 4 digit number: ")
        if len(guess) == len(random_number):
            for i in range(0, len(guess)):
                if guess[i] == random_number[i]:
                    board[i] = random_number[i]
                    board_check = "".join(str(x) for x in board)
            else:
                lives = lives - 1
        else:
            print("Invalid number of digits. Try again a 4 digit number")
    if lives == 0:
        print('You died, sorry. The number was', random_number)
    else:
        print("Congrats! You guessed the number", random_number, "!")

    #else:
    #    print("Congrats! You guessed the number", random_number, "!")


mastermind()
