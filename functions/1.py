def validate_square_matrix(matrix: list[list]) -> bool:
  for row in matrix:
    if len(row) != len(matrix):
      return False

  return True

def reverse_matrix_diagonals(matrix: list[list]) -> list:
  if not validate_square_matrix(matrix):
    raise Exception('Invalid square matrix')

  matrix_len = len(matrix)

  for i in range(matrix_len // 2):
    matrix[i][i], matrix[matrix_len - i - 1][matrix_len - i - 1] = matrix[matrix_len - i - 1][matrix_len - i - 1], matrix[i][i]

    matrix[i][matrix_len - i - 1], matrix[matrix_len - i - 1][i] = matrix[matrix_len - i - 1][i], matrix[i][matrix_len - i - 1]

  return matrix

if __name__ == '__main__':
  try:
    matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]

    print(reverse_matrix_diagonals(matrix))
  except Exception as e:
    print(e)
