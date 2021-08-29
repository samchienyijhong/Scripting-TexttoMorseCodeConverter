# Get morse chart from https://encyclopedia2.thefreedictionary.com/List+of+Morse+Code and save to "morse.text".

# Make dictionary
with open('morses.txt') as file:
    lines = file.readlines()
    morse_dict = {line.rstrip().split('\t')[0]: line.rstrip().split('\t')[1].replace(' ', '') for line in lines}
    character_dict = {morse: character for character, morse in morse_dict.items()}


# Define function
def text_to_code(text):
    try:
        result = " ".join([morse_dict[character] for character in text])
    except KeyError:
        result = f'Your input "{text}" contains invalid character!'
    return result


def code_to_text(code):
    try:
        print(code.split())
        result = "".join([character_dict[morse] for morse in code.split()])
    except KeyError:
        result = f'Your input "{code}" contains invalid morse code!'
    return result


choice = input("Code or Decode? ").lower()

if choice == 'code':
    key_in = input("Please key in text for converting to Morse code: ").upper()
    output = text_to_code(key_in)
elif choice == 'decode':
    key_in = input("Please key in Morse code for converting to text: ")
    output = code_to_text(key_in)
else:
    output = "Please enter a valid choice"

print(output)
