import random

words = ["apple", "mouse", "keydoard", "truck"]

max_tries = 7
the_word = random.choice(words)
guessed=[]
wrong_guess = 0

print("\nWelcome to game of word (guess the word)")
print("_ "*len(the_word))

while wrong_guess < max_tries:
    guess = input("\nGuess a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print ("Invalid input dingle letter only...")
        continue
    if guess in guessed:
        print(("you already guessed it"))
        continue
    guessed.append(guess)

    if guess in the_word:
        print("Correct Guess")
    else:
        print ("Wrong guess")
        wrong_guess += 1
        print("remaining chances:", max_tries - wrong_guess)

    display = [letters if letters in guessed else "_"for letters in the_word]

    print("".join(display))

    if "_" not in display:
        print ("You Won! *poping*, The word was:", the_word)
        break
else:
    print("you lost, the word was:", the_word)








