CODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.' 
}

def to_morse(message:str)->str:
    '''
    Recibe una cadena y devuelve su equivalente en código morse.
    Si algún carácter de la cadena no forma parte del diccionario de códigos, lo ignora.
    Controla el uso de mayúsculas y minúsculas.
    No normaliza los signos ortográficos.
    '''
    has_char = True in [char.upper() in CODE for char in message]
    morse_message = ''
    if has_char:
        for char in message.upper():
            if char == ' ':
                morse_message += '/ '
            for key in CODE:
                if key == char:
                    morse_message += (CODE[key] + ' ')
                    break
    return morse_message.strip()

def to_string(morse:str)->str:
    '''
    Recibe una cadena en código morse y devuelve su equivalente en cadena.
    '''
    message = ''
    if morse != '':
        morse_message = morse.split(' ')
        for char in morse_message:
            if char != '/':
                for key in CODE:
                    if CODE[key] == char:
                        message += key
                        break
            else:
                message += ' '
    return message

def input_message(prompt:str)->str:
    '''
    Pide por consola la introducción de una cadena.
    '''
    message = input(prompt)
    return message

if __name__ == '__main__':
    msg = input_message('introduce message: ')
    print(to_morse(msg))
    print(to_string(msg))