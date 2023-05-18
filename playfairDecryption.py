from playfairEncryption import find_char_position, generate_playfair_table


def decrypt(cipher_text, key):

    # Decrypt the given cipher text using the Playfair cipher
    table = generate_playfair_table(key)
    plain_text = ''
    i = 0
    while i < len(cipher_text):
        char1 = cipher_text[i]
        char2 = cipher_text[i + 1]
        row1, col1 = find_char_position(table, char1)
        row2, col2 = find_char_position(table, char2)
        if row1 == row2:
            plain_text += table[row1][(col1 - 1) % 5]
            plain_text += table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += table[(row1 - 1) % 5][col1]
            plain_text += table[(row2 - 1) % 5][col2]
        else:
            plain_text += table[row1][col2]
            plain_text += table[row2][col1]
        i += 2
    return plain_text
