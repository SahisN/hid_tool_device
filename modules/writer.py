class Writer:
    def __init__(self):
        self.NULL_CHAR = chr(0)

        # Dictionary mapping characters to their HID keycodes
        self.HID_KEYCODES = {
        'a': 4, 'b': 5, 'c': 6, 'd': 7, 'e': 8,
        'f': 9, 'g': 10, 'h': 11, 'i': 12, 'j': 13,
        'k': 14, 'l': 15, 'm': 16, 'n': 17, 'o': 18,
        'p': 19, 'q': 20, 'r': 21, 's': 22, 't': 23,
        'u': 24, 'v': 25, 'w': 26, 'x': 27, 'y': 28,
        'z': 29,'A': 4 + 0x80, 'B': 5 + 0x80, 'C': 6 + 0x80, 'D': 7 + 0x80, 'E': 8 + 0x80,
        'F': 9 + 0x80, 'G': 10 + 0x80, 'H': 11 + 0x80, 'I': 12 + 0x80, 'J': 13 + 0x80,
        'K': 14 + 0x80, 'L': 15 + 0x80, 'M': 16 + 0x80, 'N': 17 + 0x80, 'O': 18 + 0x80,
        'P': 19 + 0x80, 'Q': 20 + 0x80, 'R': 21 + 0x80, 'S': 22 + 0x80, 'T': 23 + 0x80,
        'U': 24 + 0x80, 'V': 25 + 0x80, 'W': 26 + 0x80, 'X': 27 + 0x80, 'Y': 28 + 0x80,
        'Z': 29 + 0x80,'0': 39, '1': 30, '2': 31, '3': 32, '4': 33,
        '5': 34, '6': 35, '7': 36, '8': 37, '9': 38,
        ' ': 44,  # Space key
        '!': 1,   # ! Exclamation mark
        '"': 52,  # " Double quote
        '#': 32,  # # Pound sign
        '$': 4,   # $ Dollar sign
        '%': 5,   # % Percent
        '&': 30,  # & Ampersand
        '\'': 52, # ' Single quote
        '(': 34,  # ( Left parenthesis
        ')': 45,  # ) Right parenthesis
        '*': 33,  # * Asterisk
        '+': 46,  # + Plus
        ',': 54,  # , Comma
        '-': 45,  # - Minus
        '.': 55,  # . Period
        '/': 56,  # / Slash
        ':': 55,  # : Colon
        ';': 54,  # ; Semicolon
        '<': 36,  # < Less than
        '=': 46,  # = Equal
        '>': 37,  # > Greater than
        '?': 38,  # ? Question mark
        '@': 31,  # @ At symbol
        '[': 47,  # [ Left square bracket
        '\\': 49, # \ Backslash
        ']': 48,  # ] Right square bracket
        '^': 35,  # ^ Caret
        '_': 12,  # _ Underscore
        '`': 53,  # ` Grave accent
        '{': 47 + 0x80,  # { Left curly bracket
        '|': 49 + 0x80,  # | Pipe
        '}': 48 + 0x80,  # } Right curly bracket
        '~': 53 + 0x80   # ~ Tilde
    }

    def type_string(self, str):
        with open('/dev/hidg0', 'rb+') as fd:
            for char in str:
                if char in self.HID_KEYCODES:
                    # Press the key
                    fd.write((self.NULL_CHAR*2 + chr(self.HID_KEYCODES[str]) + self.NULL_CHAR*5).encode())
                    # Release the key
                    fd.write((self.NULL_CHAR*8).encode())

