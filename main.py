# A dictionary containing all morse codes
letter_to_morse_code = {
    "A": "._",
    "B": "_...",
    "C": "_._.",
    "D": "_..",
    "E": ".",
    "F": ".._.",
    "G": "__.",
    "H": "....",
    "I": "..",
    "J": ".___",
    "K": "_._",
    "L": "._..",
    "M": "__",
    "N": "_.",
    "O": "___",
    "P": ".__,",
    "Q": "__._",
    "R": "._.",
    "S": "...",
    "T": "_",
    "U": ".._",
    "V": "..._",
    "W": ".__",
    "X": "_.._",
    "Y": "_.__",
    "Z": "__..",
    "1": ".____",
    "2": "..___",
    "3": "...__",
    "4": "...._",
    "5": ".....",
    "6": "_....",
    "7": "__...",
    "8": "___..",
    "9": "____.",
    "0": "_____",
}

morse_code_to_letter = {}
for k,v in letter_to_morse_code.items():
    morse_code_to_letter[v] = k


def converter(choice):
    result = ""
    if choice == 1:
        raw_data = input("Enter the text to convert into morse code: ").upper()
        for letter in raw_data:
            result += f"{letter_to_morse_code[letter]} "
    elif choice == 2:
        raw_data = input("Enter the morse code to convert into text using dot '.' and underscore '_': ")
        for letter in raw_data.split():
            result += morse_code_to_letter[letter]
    else:
        print("Sorry! That's not a valid option.")
        return
    print(result)


user_choice = int(input("Available Converters:\n1) Text to Morse Converter\n2) Morse to Text Converter\n\nEnter option number.\n"))
converter(user_choice)
