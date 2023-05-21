def convertDigraphsToPlainText(digraphList):
    # convert list of tuples to list of list
    listDigraph = [list(ele) for ele in digraphList]
    for i in range(len(listDigraph) - 1):
        if listDigraph[i][1] == 'X' and listDigraph[i][0] == listDigraph[i+1][0]:
            listDigraph[i][1] = listDigraph[i][1].replace('X', '')
        elif listDigraph[-1][1] == 'X':
            listDigraph[-1][1] = listDigraph[-1][1].replace('X', '')
        else:
            pass

    listDigraph = [y for x in listDigraph for y in x]

    return ''.join(listDigraph)

