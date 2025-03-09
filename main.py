import os
import pandas as pd

# Loading Audio files for morse
short_file = "sounds/beep_short.wav"
long_file = "sounds/beep_long.wav"

# Read Morse CSV File
data = pd.read_csv("files/morse.csv")
dictionary = dict(zip(data['Letter'], data['Morse']))

morse_tool = True
while morse_tool:
    # Ask user for a word to be translated, add individual letters to a list
    user_input = input("What would you like to have translated to Morse? ").upper()
    if not user_input.isalnum():
        continue

    morse_list = [dictionary[letter] for letter in user_input]

    # Go through each letter, and look up morse. For each component in Morse, play short or long beep
    for code in morse_list:
        for item in code:
            os.system("afplay " + long_file) if item == '-' else os.system("afplay " + short_file)

    # Print string of the morse code with space separators
    print(f"The Morse translation is: {" ".join(morse_list)}")

    # Check if user wants another word translated, end program if not, otherwise rerun
    check_for_more = input("Do you want to do another, Y/N? ").upper()
    morse_tool = False if check_for_more != "Y" else True
