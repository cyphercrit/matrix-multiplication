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
  def insert(self, value: int, row: int, col: int) -> bool:
    try:
      self.matrix[row - 1][col - 1] = value
      return True
    except IndexError:
      return False


if __name__ == "__main__":
  my_matrix = Matrix(2, 2)
  my_matrix.insert(2, 2, 2)
  my_matrix.print()



