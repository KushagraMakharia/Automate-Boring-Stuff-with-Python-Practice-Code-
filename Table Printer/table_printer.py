tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    row_length = []

    for col in tableData:
        row_length.append(len(col))

    table_row = max(row_length)
    table_column = len(tableData)


    line_text = ""

    for r in range(table_row):
        for c in range(table_column):
            try:
                line_text = line_text + " " + tableData[c][r]
            except IndexError:
                line_text = line_text + " "
        print(line_text)
        line_text = ""


printTable(tableData)
