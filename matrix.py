class Matrix:
  def __init__(self, rows: int, cols: int):
    self.rows = rows
    self.cols = cols

    # initialize matrix of rows x cols size
    self.matrix = [[None for _ in range(cols)] for _ in range(rows)]

  # prints visual representation of the matrix
  def print(self) -> None:
    for row in self.matrix:
      print(row)

  # inserts element into matrix at specific index, replacing if neccesary 
  def insert(self, value: int, row: int, col: int) -> None:
    if row < 1 or row > self.rows or col < 1 or col > self.cols:
      raise IndexError('Row or column index out of bounds')
    self.matrix[row - 1][col - 1] = value
  
  # multiplies every element in a matrix by a scalar, returning a new matrix
  def scalar_multiply(self, scalar: int) -> 'Matrix':
    result = Matrix(self.rows, self.cols)

    for i in range(self.rows):
      for j in (range(self.cols)):
        result.matrix[i][j] = self.matrix[i][j] * scalar
    
    return result

  # performs a multiplication of two matrices, returning a new matrix
  def matrix_multiply(self, matrix_multiple: 'Matrix') -> 'Matrix':
    pass

if __name__ == "__main__":
  my_matrix = Matrix(2, 2)
  value = 1
  for i in range(1, 3):
    for j in range(1, 3):
      my_matrix.insert(value, i, j)
      value += 1

  new_matrix = my_matrix.scalar_multiply(2)

  my_matrix.print()
  new_matrix.print()



