import random

def hangman_game():
    words = ['python', 'programming', 'challenge', 'computer', 'algorithm']
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_letters = []

    while True:
        masked_word = []
        for letter in word_to_guess:
            if letter in guessed_letters:
                masked_word.append(letter)
            else:
                masked_word.append('_')

        print('\nWord:', ' '.join(masked_word))
        print('Incorrect letters:', ' '.join(incorrect_letters))

        if '_' not in masked_word:
            print('\nCongratulations, you guessed the word!')
            break

        guess = input('Enter a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single valid letter.')
            continue

        if guess in guessed_letters or guess in incorrect_letters:
            print('You already guessed that letter.')
            continue

        if guess in word_to_guess:
            guessed_letters.append(guess)
        else:
            incorrect_letters.append(guess)

        if len(incorrect_letters) == 6:
            print('\nSorry, you lost. The word was:', word_to_guess)
            break

hangman_game()