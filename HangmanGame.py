import random
words=['python', 'java', 'c', 'os', 'c++']
word=random.choice(words)
guessed=[]         #Store guessed letter
wrong=0 # Count wrong guesses
print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
while wrong < 6:
    # Display the word
    print("\nWord:", end=" ")
    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
    guess = input("Guess a letter: ").lower()   #Store guessed lette
    if guess in guessed:
        print("You already guessed that letter!")
    elif guess in word:  # Check correct or wrong
        print("Correct!")
        guessed.append(guess)
    else:
        print("Wrong!")
        wrong = wrong + 1
        print("Wrong guesses:", wrong)

    complete = True
    for letter in word:
        if letter not in guessed:
            complete = False
    if complete:
        print("\n🎉 You Won!")
        print("The word was:", word)
        break
if wrong == 6:
    print("\nGame Over!")
    print("The word was:", word)
    
