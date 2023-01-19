import random
from words import word_list


#randomly select a word from the word list
def word_select():
  word = random.choice(word_list)
  return word.upper()


#create play rules and functions
def start(word):
  word_progress = "_" * len(word)
  guessed = False
  attempted_letters = []
  attempted_words = []
  attempts = 6
  #start game message displaying frame of hangman and the word progress
  print("Game Start!")
  print(print_hangman(attempts))
  print(word_progress)
  print("\n")
  #condition on if not guessed and still got attempts request input from user
  while not guessed and attempts > 0:
    #request input from user
    guess = input("Guess(Letter or word): ").upper()
    #for when user guesses letter
    if len(guess) == 1 and guess.isalpha():
      #check if the letter has already been guessed
      if guess in attempted_letters:
        print("You have already attempted this letter")
      #for when the guessed letter is not in the word attemps -1
      elif guess not in word:
        print(guess, "is not in the word")
        attempts -= 1
        attempted_letters.append(guess)
      #for when the guessed letter is in the word
      else:
        print("Good job, ", guess, "is in the word")
        #add the attempt to the attempted letters
        attempted_letters.append(guess)
        word_as_list = list(word_progress)
        indices = [i for i, letter in enumerate(word) if letter == guess]
        for index in indices:
          word_as_list[index] = guess
        word_progress = "".join(word_as_list)
        if "_" not in word_progress:
          guessed = True
    #for when user guessed word
    elif len(guess) == len(word) and guess.isalpha():
      #check if guess has been attempted already
      if guess in attempted_words:
        print("You have already attempted this word")
      #if guess is not the word_list
      elif guess != word:
        print(guess, "is not the correct word")
        attempts -= 1
        #add the attempt to the attempted words
        attempted_words.append(guess)
      #if guess is correct
      else:
        guessed = True
        #show the word
        word_progress = word
    #for when user does not input a valid guess
    else:
      print("This is not a valid guess.")
    #after each attempts, print out the new frame according to the number of attempts and also the updated word_progress
    print(print_hangman(attempts))
    print(word_progress)
    print("\n")

  #when user guessed the word correcty
  if guessed:
    print("Congratulations, you've guessed the word!")
  else:
    print("Ran out of attempts. the word was", word, ".Try again ! :)")


def print_hangman(attempts):
  if (attempts == 6):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif (attempts == 5):
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif (attempts == 4):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif (attempts == 3):
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif (attempts == 2):
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif (attempts == 1):
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif (attempts == 0):
    print(" O  |")
    print("/|\ |")
    print("/ \ |")
    print("   ===")


def main():
  word = word_select()
  start(word)
  while input("Play Again? (Y/N) ").upper() == "Y":
    word = word_select()
    start(word)


if __name__ == "__main__":
  main()
