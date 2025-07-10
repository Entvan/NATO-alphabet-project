import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

with open("nato_phonetic_alphabet.csv") as file:
    alphabet_file = pandas.read_csv(file)

    alphabet_file_frame = pandas.DataFrame(alphabet_file)

    alphabet_dictionary = {row.letter: row.code for (index, row) in alphabet_file_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while True:
    word_input = input("Enter a word: ").upper()
    if word_input == "EXIT":
        break

    result = [alphabet_dictionary[letter] for letter in word_input]
    print(result)

