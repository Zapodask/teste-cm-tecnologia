def validate_matrix(matrix: list[list]) -> bool:
  for row in matrix:
    if len(row) != len(matrix[0]):
      return False

  return True

def is_submatrix(matrix: list[list], submatrix: list[list], i: int, j: int) -> bool:
  for row in range(len(submatrix)):
    for col in range(len(submatrix)):
      if matrix[i + row][j + col] != submatrix[row][col]:
        return False

  return True

def count_submatrix(matrix: list[list], submatrix: list[list]) -> int:
  if not validate_matrix(matrix):
    raise Exception('Invalid matrix')

  if not validate_matrix(submatrix):
    raise Exception('Invalid submatrix')

  submatrix_len = len(submatrix)
  count = 0

  for i in range(len(matrix) - submatrix_len + 1):
    for j in range(len(matrix) - submatrix_len + 1):
      if is_submatrix(matrix, submatrix, i, j):
        count += 1

  return count

if __name__ == '__main__':
  try:
    matrix = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]

    submatrix = [
      [1, 2],
      [4, 5]
    ]

    print(count_submatrix(matrix, submatrix))
  except Exception as e:
    print(e)