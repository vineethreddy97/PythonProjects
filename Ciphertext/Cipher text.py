from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w','x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amount = (shift_amount) * (-1)
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text=end_text+alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    play_again=input("Type 'yes' if you want to go again . Otherwise type 'no'")
    if play_again=='no':
        should_continue=False
        print("Goodbye")


