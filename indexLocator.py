def indexLocator(char, cipherKeyMatrix):
    indexOfChar = []

    # convert the character value from J to I
    if char == "J":
        char = "I"

    for i, j in enumerate(cipherKeyMatrix):
        # enumerate will return object like this:
        # [
        #   (0, ['K', 'A', 'R', 'E', 'N']),
        #   (1, ['D', 'B', 'C', 'F', 'G']),
        #   (2, ['H', 'I', 'L', 'M', 'O']),
        #   (3, ['P', 'Q', 'S', 'T', 'U']),
        #   (4, ['V', 'W', 'X', 'Y', 'Z'])
        # ]
        # i,j will map to tuples of above array

        # j refers to inside matrix =>  ['K', 'A', 'R', 'E', 'N'],
        for k, l in enumerate(j):
            # again enumerate will return object that look like this in first iteration:
            # [(0,'K'),(1,'A'),(2,'R'),(3,'E'),(4,'N')]
            # k,l will map to tuples of above array
            if char == l:
                indexOfChar.append(i)  # add 1st dimension of 5X5 matrix => i.e., indexOfChar = [i]
                indexOfChar.append(k)  # add 2nd dimension of 5X5 matrix => i.e., indexOfChar = [i,k]
                return indexOfChar

            # Now with the help of indexOfChar = [i,k] we can pretty much locate every element,
            # inside our 5X5 matrix like this =>  cipherKeyMatrix[i][k]
