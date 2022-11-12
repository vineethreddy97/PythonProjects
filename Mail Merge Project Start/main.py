PLACEHOLDER="[name]"
with open("./Input/Names/invited_names.txt") as names_files:
    names=names_files.readlines()# to make into list

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_name=letter_file.read()
    for name in names:
        Stripped_name=name.strip()# To removes extra spaces
        new_letter=letter_name.replace(PLACEHOLDER,Stripped_name)# replace is used to replace different name
        with open(f"./Output/ReadyToSend/letter_for_{Stripped_name}.txt",mode="w") as completed_file:
            completed_file.write(new_letter)


