
import random
from hangman_words import word_list
from hangman_art import *

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#printing logo from the imported module
print(logo)

#Create blanks
display = list()
for _ in range(word_length):
    display += "_"

guessed = list()

# while loop to run until the user lives is 0 or user has correctly guessed the word
while not end_of_game:
  
  guess = input("Guess a letter: ").lower()

  # checking if the user already guessed the letter 
  if guess in display:
    print(f"you have already guessed: {guess}")
  elif guess in guessed:
    lives +=1

  guessed.append(guess)
   
    #Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
 
    #checks if the user entered chouce is present in the word or not 
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word")
    lives -= 1
    
  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("Congratulations, You Win!!!")

  #checks if lives value is 0 if yes then end the game and exit out of the loop and print "you lose" 
  if(lives == 0):
    end_of_game = True
    print("Tough Luck, You Lose")
    print(f"The word was {chosen_word}")
  

  # prints the stages of how many lives user has until he is hanged
  print(stages[lives])
  
  