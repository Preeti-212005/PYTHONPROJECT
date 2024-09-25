import random
def guess_the_number():
    number = random.randint(1, 100)  # Generate random number
    attempts = 10  # Maximum attempts
    
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number.")
            break
        
        attempts -= 1
        print(f"Remaining attempts: {attempts}")
    
    if attempts == 0:
        print(f"Sorry, you're out of attempts. The number was {number}.")
import tkinter as tk
import random

def check_guess():
    guess = int(entry.get())
    if guess < number:
        result_label.config(text="Too low!")
    elif guess > number:
        result_label.config(text="Too high!")
    else:
        result_label.config(text="Correct! You guessed it!")

def new_game():
    global number
    number = random.randint(1, 100)
    result_label.config(text="")


root = tk.Tk()
root.title("Guess the Number")


number = random.randint(1, 100)
instruction = tk.Label(root, text="Guess a number between 1 and 100")
instruction.pack()

entry = tk.Entry(root)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=check_guess)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.pack()


root.mainloop()
