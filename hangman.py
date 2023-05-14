import random


def choose_word():
    """Choose a random word from a list of words."""
    with open('bandNames.txt', 'r') as file:
        words = file.read().splitlines()
    return random.choice(words)


def initialize_guessed_word(word):
    """Initialize the guessed word with underscores."""
    return "_" * len(word)


def get_guess(guessed_letters):
    """Get a letter guess from the player."""
    guess = input("Guess a letter: ").lower().strip()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        return None
    return guess


def update_guessed_word(word, guessed_word, guess):
    """Update the guessed word with the correctly guessed letter."""
    new_guessed_word = ""
    for i in range(len(word)):
        if word[i] == guess:
            new_guessed_word += guess
        elif word[i] == " ":
            new_guessed_word += " "
        else:
            new_guessed_word += guessed_word[i]
    return new_guessed_word


def update_guesses_remaining(word, guess, guesses_remaining):
    """Update the number of guesses remaining."""
    if guess not in word:
        guesses_remaining -= 1
    return guesses_remaining


def display_game_status(guessed_word, guesses_remaining, guessed_letters):
    """Display the current status of the game."""
    print(f"\n{guessed_word}")
    print(f"Guesses remaining: {guesses_remaining}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")


def is_game_over(word, guessed_word, guesses_remaining):
    """Check if the game is over."""
    return guessed_word == word or guesses_remaining == 0


def print_initial_message():
    print("#" * 35 + "\n" +
          "Let's play Hangman ☻♫ - Metal Bands!\n" +
          "#" * 35)


def print_win_message(word):
    print(f"\nCongratulations! You guessed the word '{word}!'")


def print_lose_message(word):
    print(f"\nSorry, you ran out of guesses. The word was '{word}'.")


def play_hangman():
    print_initial_message()
    # Play the hangman game ☺#
    word = choose_word()
    guessed_word = initialize_guessed_word(word)
    guesses_remaining = 6
    guessed_letters = set()

    while not is_game_over(word, guessed_word, guesses_remaining):
        display_game_status(guessed_word, guesses_remaining, guessed_letters)
        guess = get_guess(guessed_letters)
        if guess is None:
            continue
        guessed_letters.add(guess)
        guessed_word = update_guessed_word(word, guessed_word, guess)
        guesses_remaining = update_guesses_remaining(word, guess, guesses_remaining)

    if guessed_word == word:
        print_win_message(word)
    else:
        print_lose_message(word)


if __name__ == "__main__":
    play_hangman()
