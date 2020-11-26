class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(str(l) for l in self.matrix)

    def __add__(self, other_matrix):
        other_matrix = other_matrix.matrix

        new_matrix = []
        for i in range(min(len(self.matrix), len(other_matrix))):
            new_line = []
            for j in range(min(len(self.matrix[i]), len(other_matrix[i]))):
                new_line.append(self.matrix[i][j] + other_matrix[i][j])
            new_matrix.append(new_line)

        return Matrix(new_matrix)


matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
print(matrix1)

matrix2 = Matrix([[10, 20], [30, 40], [50, 60]])
print(matrix1 + matrix2)
