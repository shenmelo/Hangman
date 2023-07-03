import random
from replit import clear
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)
display = []
end_of_game = False
lives = 6
print(f"The chosen word is {chosen_word}")

for _ in range(word_length):
  display += "_"
while not end_of_game:
  guess = input("Guess a letter: ")

  clear()

  if guess not in chosen_word:
    print(f"'{guess}' is not in chosen word. You lose a live.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      clear()
      print("You lose")

  if guess in display:
    print(f"'{guess}' is already chosen. Please pick another letter.")
  
  print(stages[lives])
  
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  
  print(f"{' '.join(display)}")
    
  if "_" not in display:
    end_of_game = True
    clear()
    print("You win.")