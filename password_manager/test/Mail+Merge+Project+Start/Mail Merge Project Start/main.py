#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_path = "test/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt"
template_path = "test/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt"
output_path = "test/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend"


with open(names_path, 'r') as file:
    names = file.readlines()

with open(template_path) as file:
    template = file.read()

for name in names:
    letter = template.replace("[name]", name.strip())
    file_name = f"{name.strip()}.txt"
    letter_path = f"{output_path}/{file_name}"
    with open(letter_path, 'w') as file:
        file.write(letter)




