import pandas

#Import the CSV with the NATO alphabet into a dictionary
alphabet_dict = {row.letter: row.code for (index,row) in
 pandas.read_csv("nato_phonetic_alphabet.csv").iterrows()}

#Get a word from the user to spell
word = input("Enter a word you want spelled according to the NATO phonetical alphabet:\n").upper()
print([alphabet_dict[letter] for letter in word])
