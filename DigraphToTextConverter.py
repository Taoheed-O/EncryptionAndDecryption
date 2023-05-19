def convertDiagraphsToPlainText(digraphList):
    # convert list of tuples to list of list
    listDigraph = [list(ele) for ele in digraphList]
    for i in range(len(listDigraph) - 1):
        if listDigraph[i][1] == 'X' and listDigraph[i][0] == listDigraph[i+1][0]:
            listDigraph[i][1] = listDigraph[i][1].replace('X', '')
        elif listDigraph[-1][1] == 'X':
            listDigraph[-1][1] = listDigraph[-1][1].replace('X', '')

    return listDigraph


print(convertDiagraphsToPlainText([('H', 'E'), ('L', 'X'), ('L', 'O'), ('W', 'O'), ('R', 'L'), ('D', 'X')]))
