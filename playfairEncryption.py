import string


def generate_playfair_table(key):

    # Create a Playfair table based on the provided key
    key = key.upper().replace('J', 'I')
    alphabet = string.ascii_uppercase.replace('J', '')
    table = []
    for char in key + alphabet:
        if char not in table and char != 'J':
            table.append(char)
    return table


def find_char_position(table, char):

    # Find the position of a character in the Playfair table
    for i, row in enumerate(table):
        for j, col in enumerate(row):
            if col == char:
                return i, j


def encrypt(plain_text, key):

    # Encrypt the given plain text using the Playfair cipher
    table = generate_playfair_table(key)
    plain_text = plain_text.upper().replace('J', 'I')
    cipher_text = ''
    i = 0
    while i < len(plain_text):
        char1 = plain_text[i]
        char2 = plain_text[i + 1] if i + 1 < len(plain_text) else 'X'
        if char1 == char2:
            char2 = 'X'
            i -= 1
        row1, col1 = find_char_position(table, char1)
        row2, col2 = find_char_position(table, char2)
        if row1 == row2:
            cipher_text += table[row1][(col1 + 1) % 5]
            cipher_text += table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += table[(row1 + 1) % 5][col1]
            cipher_text += table[(row2 + 1) % 5][col2]
        else:
            cipher_text += table[row1][col2]
            cipher_text += table[row2][col1]
        i += 2
    return cipher_text
