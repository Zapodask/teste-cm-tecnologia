from src.matrix import Matrix

def test_matrix():
  matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  assert matrix.matrix == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  assert matrix.matrix_len == 3

def test_invalid_matrix():
  try:
    Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]])
  except Exception as e:
    assert str(e) == 'Invalid square matrix'

def test_matrix_reverse_diagonals():
  matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  assert matrix.reverse_matrix_diagonals() == [[9, 2, 7], [4, 5, 6], [3, 8, 1]]

def test_matrix_reverse_diagonals_2():
  matrix = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

  assert matrix.reverse_matrix_diagonals() == [[16, 2, 3, 13], [5, 11, 10, 8], [9, 7, 6, 12], [4, 14, 15, 1]]

def test_matrix_reverse_diagonals_3():
  matrix = Matrix([[1, 2], [3, 4]])

  assert matrix.reverse_matrix_diagonals() == [[4, 3], [2, 1]]

def test_matrix_reverse_diagonals_4():
  matrix = Matrix([[1]])

  assert matrix.reverse_matrix_diagonals() == [[1]]

def test_matrix_reverse_diagonals_5():
  matrix = Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])

  assert matrix.reverse_matrix_diagonals() == [[25, 2, 3, 4, 21], [6, 19, 8, 17, 10], [11, 12, 13, 14, 15], [16, 9, 18, 7, 20], [5, 22, 23, 24, 1]]

def test_matrix_reverse_diagonals_6():
  matrix = Matrix([[1, 2, 3, 4, 5, 6], 
                   [7, 8, 9, 10, 11, 12], 
                   [13, 14, 15, 16, 17, 18], 
                   [19, 20, 21, 22, 23, 24], 
                   [25, 26, 27, 28, 29, 30], 
                   [31, 32, 33, 34, 35, 36]])

  assert matrix.reverse_matrix_diagonals() == [[36, 2, 3, 4, 5, 31], [7, 29, 9, 10, 26, 12], [13, 14, 22, 21, 17, 18], [19, 20, 16, 15, 23, 24], [25, 11, 27, 28, 8, 30], [6, 32, 33, 34, 35, 1]]
