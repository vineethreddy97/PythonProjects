import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
word_length=len(chosen_word)
for _ in range(word_length):
    display+='_'
end_of_game=False
lives=6
while not end_of_game:
    guess=input("Guess a letter").lower()
    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    print(display)
    if guess not in chosen_word:
        lives=lives-1
        if lives==0:
            end_of_game=True
            print("you loose")
    if '_' not in display:
        end_of_game=True
        print("You Win")
    print(stages[lives])