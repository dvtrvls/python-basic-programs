import pandas as pd

nato_csv = pd.read_csv("nato_phonetic_alphabet.csv")
nato_df = pd.DataFrame(nato_csv)
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

def translate(word):
    try:
        return [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")

while True:
    print("""            ███╗   ██╗ █████╗ ████████╗ ██████╗ 
            ████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗
            ██╔██╗ ██║███████║   ██║   ██║   ██║
            ██║╚██╗██║██╔══██║   ██║   ██║   ██║
            ██║ ╚████║██║  ██║   ██║   ╚██████╔╝
            ╚""")
    
    usr = input("Input your name: ").upper()
    print(translate(usr))
