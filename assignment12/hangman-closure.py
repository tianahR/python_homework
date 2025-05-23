# Task 4: Closure Practice

# Task 4:2 Declare a function called make_hangman() that has one argument called secret_word. 
# It should also declare an empty array called guesses. Within the function declare a function called hangman_closure() that takes one argument,
# which should be a letter. Within the inner function, each time it is called, the letter should be appended to the guesses array. 
# Then the word should be printed out, with underscores substituted for the letters that haven't been guessed.
# So, if secret_word is "alphabet", and guesses is ["a", "h"], then "a__ha__" should be printed out. 
# The function should return True if all the letters have been guessed, and False otherwise.
# make_hangman() should return hangman_closure.

def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter[0])
        word = []
        all_guessed = True
        for char in secret_word:
            if char in guesses:
                word.append(char)
            else:
                all_guessed = False
                word.append("_")
        print("".join(word))
        return all_guessed
    return hangman_closure 

# Task 4:3 Within hangman-closure.py, implement a hangman game that uses make_hangman(). Use the input() function to prompt for the secret word. 
# Then use the input() function to prompt for each of the guesses, until the full word is guessed.

secret_word = input("What is the secret word? ")
game = make_hangman(secret_word)
all_guessed = False
while not all_guessed:
    letter = input("What letter do you guess? ")
    all_guessed = game(letter)
    