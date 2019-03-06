tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    #Store longest item in each list
    colWidths = [0] * len(tableData)

    #Find longest item in each list
    for item in range(len(table[0])):
        for column in range(len(table)):
            if colWidths[column]<=len(table[column][item]):
                colWidths[column]=len(table[column][item])
                    

    #Print out table with each column rjusted
    for item in range(len(table[0])):
        for column in range(len(table)):
            print(table[column][item].rjust(colWidths[column]),end=" ")
        print()


printTable(tableData)

