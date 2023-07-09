class Matrix:
  def __init__(self, matrix: list[list]) -> None:
    is_square_matrix = self.__validate_square_matrix(matrix)

    if not is_square_matrix:
      raise Exception('Invalid square matrix')

    self.matrix = matrix
    self.matrix_len = len(matrix)

  def __validate_square_matrix(self, matrix: list[list]) -> bool:
    for row in matrix:
      if len(row) != len(matrix):
        return False

    return True

  def reverse_matrix_diagonals(self) -> list:
    for i in range(self.matrix_len // 2):
      self.matrix[i][i], self.matrix[self.matrix_len - i - 1][self.matrix_len - i - 1] = self.matrix[self.matrix_len - i - 1][self.matrix_len - i - 1], self.matrix[i][i]

      self.matrix[i][self.matrix_len - i - 1], self.matrix[self.matrix_len - i - 1][i] = self.matrix[self.matrix_len - i - 1][i], self.matrix[i][self.matrix_len - i - 1]

    return self.matrix
