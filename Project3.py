import random


WORDS = ['python', 'development', 'hangman', 'challenge', 'programming', 'debugging']


def choose_word():
    return random.choice(WORDS)


def display_word(word, correct_guesses):
    display = [letter if letter in correct_guesses else '_' for letter in word]
    return ' '.join(display)


def hangman():
    word = choose_word()
    correct_guesses = set()
    incorrect_guesses = set()
    attempts_remaining = 6

    print("Welcome to Hangman Challenge!")
    print("Guess the word, one letter at a time.")
    print(f"The word has {len(word)} letters.")
    
    while attempts_remaining > 0:
        print("\nCurrent word state:", display_word(word, correct_guesses))
        print(f"Incorrect guesses: {', '.join(sorted(incorrect_guesses))}")
        print(f"Attempts remaining: {attempts_remaining}")
        
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a valid letter.")
            continue
        
        if guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter. Try again.")
            continue

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            correct_guesses.add(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses.add(guess)
            attempts_remaining -= 1

        if all(letter in correct_guesses for letter in word):
            print(f"\nCongratulations! You guessed the word '{word}' correctly!")
            break
    else:
        print(f"\nGame over! You ran out of attempts. The word was '{word}'.")


if __name__ == "__main__":
    hangman()
