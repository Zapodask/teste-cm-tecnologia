class Matrix:
  def __init__(self, matrix: list[list]) -> None:
    is_matrix = self.__validate_matrix(matrix)

    if not is_matrix:
      raise Exception('Invalid matrix')

    self.matrix = matrix
    self.matrix_len = len(matrix)

  def __validate_matrix(self, matrix: list[list]) -> bool:
    for row in matrix:
      if len(row) != len(matrix[0]):
        return False

    return True

  def __is_submatrix(self, submatrix: list[list], i: int, j: int) -> bool:
    for row in range(len(submatrix)):
      for col in range(len(submatrix)):
        if self.matrix[i + row][j + col] != submatrix[row][col]:
          return False

    return True

  def count_submatrix(self, submatrix: list[list]) -> int:
    if not self.__validate_matrix(submatrix):
      raise Exception('Invalid submatrix')

    submatrix_len = len(submatrix)
    count = 0

    for i in range(self.matrix_len - submatrix_len + 1):
      for j in range(self.matrix_len - submatrix_len + 1):
        if self.__is_submatrix(submatrix, i, j):
          count += 1

    return count
