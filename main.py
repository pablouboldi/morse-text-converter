import time
import winsound


def dot():
    winsound.Beep(440, int(TIME_UNIT * 1000))
    return


def dash():
    winsound.Beep(440, int(TIME_UNIT * 3000))
    return


def morse_to_text(string):
    translated_code = ''
    words = string.split()
    for word in words:
        letters = word.split('/')
        for letter in letters:
            translated_code += MORSE_TO_TEXT[letter]
        translated_code += MORSE_TO_TEXT[' ']

    return translated_code


def text_to_morse(string):
    translated_text = ''

    for char in string:
        translated_text += TEXT_TO_MORSE[char] + ' '

    return translated_text


def sounds():
    try:
        for char in morse_code:
            if char == '.':
                dot()
                time.sleep(TIME_UNIT)
            elif char == '-':
                dash()
                time.sleep(TIME_UNIT)
            elif char == ' ':
                time.sleep(TIME_UNIT * 3)
    except NameError:
        return
    else:
        return


def main():
    global morse_code
    is_valid = False

    while not is_valid:

        user_choice = input('Would you like to transform MORSE TO TEXT (1) or TEXT TO MORSE (2)?\n')

        if int(user_choice) == 1:
            is_valid = True
            user_input = input('Please, enter the morse code you want translated with "/" between each letter and "spaces" between each word:\n')
            text_code = morse_to_text(user_input).upper()
            print(f'\nThe translated text is:\n{text_code}')

        elif int(user_choice) == 2:
            is_valid = True
            user_input = input('Please, give the text you want translated:\n').upper()
            morse_code = text_to_morse(user_input)
            print(f'The Morse code is:\n{morse_code}')

        else:
            print("You didn't give a valid answer. Try again:\n")

    sounds()


TIME_UNIT = 0.1

TEXT_TO_MORSE = {'A': '.-', 'B': '-...',
                 'C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-',
                 'L': '.-..', 'M': '--', 'N': '-.',
                 'O': '---', 'P': '.--.', 'Q': '--.-',
                 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--',
                 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                 '1': '.----', '2': '..---', '3': '...--',
                 '4': '....-', '5': '.....', '6': '-....',
                 '7': '--...', '8': '---..', '9': '----.',
                 '0': '-----', ',': '--..--', '.': '.-.-.-',
                 '?': '..--..', '/': '-..-.', '-': '-....-',
                 '(': '-.--.', ')': '-.--.-', ' ': ' '
                 }

MORSE_TO_TEXT = {value: key for key, value in TEXT_TO_MORSE.items()}

main()
