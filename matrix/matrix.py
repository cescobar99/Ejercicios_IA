class Matrix:
    def __init__(self, matrix_string):
        matrix_string = matrix_string.split("\n")
        self.matrix_string = [[int(y) for y in x.split()] for x in matrix_string]
    
        print(matrix_string)        
      

    def row(self, index):
        row = []
        for i in range(len(self.matrix_string)):
            row.append(self.matrix_string[i])
        row = row[index -1]
        return row

    def column(self, index):
        column = []
        for i in range(len(self.matrix_string)):
            column.append(self.matrix_string[i][index-1])
        return column

