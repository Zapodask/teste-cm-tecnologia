from read_input_file import read_input_file
from matrix import Matrix

def main():
  file = read_input_file()

  matrix = Matrix(file.matrix)

  return matrix.count_submatrix(file.submatrix)

if __name__ == '__main__':
  try:
    print(main())
  except Exception as e:
    print(e)
