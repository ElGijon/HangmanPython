
# Hangman Game / (Jogo da Forca) - Python

Project developed along with the Python course of the platform Alura

Projeto desenvolvido juntamente ao curso de Python da plataforma Alura



## Proposed Learning /  Aprendizados propostos 

Develop the popular hangman game system using basic Python concepts

Desenvolver um sistema do popular jogo da forca utilizando conceitos básicos do Python



## Improvements / Melhorias 
English:

This Python project is a text-based Hangman game that focuses on Metal Bands. It includes the following elements:

    Importing Modules: The random module is imported to choose a random word.

    choose_word() Function: This function reads a list of words from a file (bandNames.txt) and selects a random word from the list.

    initialize_guessed_word(word) Function: This function takes a word as input and initializes the guessed word with underscores to represent the hidden letters.

    get_guess(guessed_letters) Function: This function prompts the player to guess a letter, converts the input to lowercase, and checks if the letter has already been guessed.

    update_guessed_word(word, guessed_word, guess) Function: This function updates the guessed word by replacing the underscores with correctly guessed letters.

    update_guesses_remaining(word, guess, guesses_remaining) Function: This function updates the number of guesses remaining based on whether the guess is correct or not.

    display_game_status(guessed_word, guesses_remaining, guessed_letters) Function: This function displays the current status of the game, including the guessed word, number of guesses remaining, and the letters that have been guessed.

    is_game_over(word, guessed_word, guesses_remaining) Function: This function checks if the game is over by comparing the guessed word with the actual word or if there are no more guesses remaining.

    Printing Messages: There are functions to print initial messages, win messages, and lose messages.

    play_hangman() Function: This function is the main game loop that initializes the game, prompts the player for guesses, updates the game status, and checks if the game is over.

    if __name__ == "__main__":: This condition ensures that the play_hangman() function is executed only when the script is run directly and not when it is imported as a module.

This project demonstrates the use of functions, loops, conditionals, file I/O, string manipulation, and module import in Python.

-----------------------------------

Português:

Este projeto Python é um jogo da forca text-based que se centra em bandas de metal. Ele inclui os seguintes elementos:

    Importando módulos: O módulo random é importado para escolher uma palavra aleatória.

    Função choose_word(): Esta função lê uma lista de palavras de um ficheiro (bandNames.txt) e seleciona uma palavra aleatória da lista.

    Função initialize_guessed_word(word) : Esta função recebe uma palavra como entrada e inicializa a palavra adivinhada com underscores para representar as letras ocultas.

    Função get_guess(letras_adivinhadas) : Esta função pede ao jogador para adivinhar uma letra, converte a entrada para minúsculas e verifica se a letra já foi adivinhada.

    update_guessed_word(word, guessed_word, guess) Função: Esta função actualiza a palavra adivinhada, substituindo os sublinhados por letras adivinhadas correctamente.

    update_guesses_remaining(word, guess, guesses_remaining) Função: Esta função actualiza o número de palpites restantes com base no facto de o palpite estar correcto ou não.

    display_game_status(palavra_adivinhada, adivinhas_restantes, letras_adivinhadas) Função: Esta função mostra o estado actual do jogo, incluindo a palavra adivinhada, o número de tentativas restantes e as letras que foram adivinhadas.

    is_game_over(palavra, palavra_adivinhada, letras_adivinhadas) Função: Esta função verifica se o jogo terminou, comparando a palavra adivinhada com a palavra actual ou se não há mais adivinhas.

    Impressão de mensagens: Existem funções para imprimir mensagens iniciais, mensagens de vitória e mensagens de derrota.

    Função play_hangman(): Esta função é o loop principal do jogo que inicializa o jogo, pede palpites ao jogador, actualiza o estado do jogo e verifica se o jogo terminou.

    if __name__ == "__main__":: Esta condição assegura que a função play_hangman() é executada apenas quando o script é executado directamente e não quando é importado como um módulo.

Este projecto demonstra o uso de funções, loops, condicionais, E/S de ficheiros, manipulação de strings e importação de módulos em Python.
