LETTERS = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
  'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1',
   '2', '3', '4', '5', '6', '7', '8', '9', '0']
MORSE_CODE = [" ", ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",  "--", "-.", "---", ".--.", "--.-", ".-.", "...", "_", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]

DEBUG = False

def ConvertToMorse(textToChange):
    newText = ""
    textToChange = textToChange.lower()
    if DEBUG: print(textToChange)
    for i in range(len(textToChange)):
        if DEBUG: print(textToChange[i])
        for j in range(len(LETTERS)):
            if textToChange[i] == LETTERS[j]:
                if DEBUG: print(MORSE_CODE[j])
                newText += MORSE_CODE[j]
                newText += " "
                break
    return newText