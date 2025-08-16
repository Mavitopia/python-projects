# NOTE 1: HANGMAN_PICS holds the ASCII-art stages (index 0 = no mistakes, last index = final state).
# NOTE 2: `wrong_attempts` counts incorrect guesses; when it reaches 6 the game ends.

HANGMAN_PICS = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#IMPORTS
from random_word import RandomWords

#FUNCS
def get_single_letter(prompt="Enter a letter: "):
    while True:
        user_input = input(prompt).strip().lower()  # remove spaces and convert to lowercase
        if len(user_input) != 1:
            print("Please enter only a single letter.")
        elif not user_input.isalpha():
            print("Only letters (a-z) are allowed.")
        else:
            return user_input  # valid single letter
        

def prompt_player(mistake_count, repeated, word):
    if not repeated:
        if mistake_count == 0:
            print(f"Welcome to the Hangman game! Your goal is to guess the hidden word within 6 attempts before the man is hanged. Good luck!\n{HANGMAN_PICS[0]}")
            player_guess_input = get_single_letter(f"Letters guessed so far: {' '.join(masked_letters)}\n\nYour guess: ")
        elif mistake_count == 1:
            print(f"Great start! Keep guessing carefully to reveal the hidden word. You still have plenty of chances.\n{HANGMAN_PICS[1]}")
            player_guess_input = get_single_letter(f"Letters guessed so far: {' '.join(masked_letters)}\n\nYour guess: ")
        elif mistake_count == 2:
            print(f"Keep going! You still have a chance. Guess the word carefully.\n{HANGMAN_PICS[2]}")
            player_guess_input = get_single_letter(f"Letters guessed so far: {' '.join(masked_letters)}\n\nYour guess: ")
        elif mistake_count == 3:
            print(f"You're halfway there! Stay focused.\n{HANGMAN_PICS[3]}")
            player_guess_input = get_single_letter(f"Letters guessed so far: {' '.join(masked_letters)}\n\nYour guess: ")
        elif mistake_count == 4:
            print(f"Be careful! Only a few attempts left.\n{HANGMAN_PICS[4]}")
            player_guess_input = get_single_letter(f"Letters guessed so far: {' '.join(masked_letters)}\n\nYour guess: ")
        elif mistake_count == 5:
            print(f"This is it! One last chance to guess the word correctly.\n{HANGMAN_PICS[5]}")
            player_guess_input = get_single_letter(f"Letters guessed so far: {' '.join(masked_letters)}\n\nYour guess: ")
        elif mistake_count >= 6:
            print(f"Game over! The man has been hanged.\n{HANGMAN_PICS[6]} \n the word was: {word}")
            return ""

        return player_guess_input.lower()
    else:
        player_guess_input = get_single_letter(f"You have already gussed this letter! \n Letters guessed so far: {' '.join(masked_letters)}\n\nYour guess: ")
        return player_guess_input.lower()
    
#VARS
random_word_generator = RandomWords()
secret_word = random_word_generator.get_random_word()

is_game_active = True
wrong_attempts = 0

masked_letters = []

for i in secret_word:
    masked_letters.append("_")

repeated_guess = False

correct_letters = []

#Game
while is_game_active:

    # DEBUG: Uncomment the following line to reveal the secret word for testing purposes
    # print(secret_word)

    player_guess = prompt_player(wrong_attempts, repeated_guess, secret_word)
    repeated_guess = False #back to default

    if (wrong_attempts >= 6):
        is_game_active = False
        break
    

    if player_guess in secret_word:
        if player_guess in correct_letters:
            repeated_guess = True
        else:
            correct_letters.append(player_guess)
            masked_letters = [letter if letter in correct_letters else "_" for letter in secret_word]
    else:
        wrong_attempts += 1
    
    current_guess = "".join(masked_letters)

    #check if user guessed the word
    if current_guess == secret_word:
        print("YOU WON")
        is_game_active = False
        break
    
