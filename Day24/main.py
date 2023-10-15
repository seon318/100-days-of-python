#TODO: Create a letter using starting_letter.txt

with open("Input/Letters/starting_letter.txt", "r") as letter:
    letter_contents = letter.read()

    with open("Input/Names/invited_names.txt", "r") as name:
        name_list = name.readlines()

for i in name_list:
    with open(f"Output/ReadyToSend/{i.strip()}.txt", "w") as output:
        output.write(letter_contents.replace('[name]', i.strip()))
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp