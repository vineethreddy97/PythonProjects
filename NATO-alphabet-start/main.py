
import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")

data_dictnoary={row.letter:row.code for(index,row) in data.iterrows()}
#print(data_dictnoary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_game_on=True
while is_game_on:
    word=input("Enter the word:").upper()
    if word =="#":
        is_game_on=False
    else:
        output_list=[data_dictnoary[letter] for letter in word]
        print(output_list)
