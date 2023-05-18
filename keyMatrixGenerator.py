def generateKeyMatrix(key):

    # Initially Create 5X5 matrix with all values as 0
    # [
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0],
    #   [0, 0, 0, 0, 0]
    # ]
    matrix_5x5 = [[0 for i in range(5)] for j in range(5)]

    simpleKeyArr = []

    """
     Generate SimpleKeyArray with key from user Input 
     with following below condition:
     1. Character Should not be repeated again
     2. Replacing J as I (as per rule of playfair cipher)
    """
    for c in key:
        if c not in simpleKeyArr:
            if c == 'J':
                simpleKeyArr.append('I')
            else:
                simpleKeyArr.append(c)

    """
    Fill the remaining SimpleKeyArray with rest of unused letters from english alphabets 
    """

    is_I_exist = "I" in simpleKeyArr

    # A-Z's ASCII Value lies between 65 to 90 but as range's second parameter excludes that value we will use 65 to 91
    for i in range(65, 91):
        if chr(i) not in simpleKeyArr:
            # I = 73
            # J = 74
            # We want I in simpleKeyArr not J

            if i == 73 and not is_I_exist:
                simpleKeyArr.append("I")
                is_I_exist = True
            elif i == 73 or i == 74 and is_I_exist:
                pass
            else:
                simpleKeyArr.append(chr(i))

    """
    Now map simpleKeyArr to matrix_5x5 
    """
    index = 0
    for i in range(0, 5):
        for j in range(0, 5):
            matrix_5x5[i][j] = simpleKeyArr[index]
            index += 1

    return matrix_5x5
