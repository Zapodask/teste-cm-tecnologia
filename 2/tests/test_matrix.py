import pytest

from src.matrix import Matrix

def test_matrix():
  matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  assert matrix.matrix == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  assert matrix.matrix_len == 3

def test_invalid_matrix():
  try:
    Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]])
  except Exception as e:
    assert str(e) == 'Invalid matrix'

def test_count_submatrix_single_match():
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    submatrix = [[2, 3], [5, 6]]
    assert matrix.count_submatrix(submatrix) == 1

def test_count_submatrix_multiple_matches():
    matrix = Matrix([[1, 2, 5, 2], [4, 5, 2, 5], [2, 5, 2, 5], [5, 2, 5, 2]])
    submatrix = [[2, 5], [5, 2]]
    assert matrix.count_submatrix(submatrix) == 3

def test_count_submatrix_no_match():
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    submatrix = [[9, 8], [6, 5]]
    assert matrix.count_submatrix(submatrix) == 0

def test_count_submatrix_invalid_submatrix():
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    invalid_submatrix = [[1, 2, 3], [4, 5, 6, 7]]
    with pytest.raises(Exception, match='Invalid submatrix'):
        matrix.count_submatrix(invalid_submatrix)