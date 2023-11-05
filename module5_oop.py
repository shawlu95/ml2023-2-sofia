# Create a class called Numbers
# the class should have 3 methods:
# 1. __init__ - the constructor
# 2. read_numbers - reads N numbers from the user
# 3. find_x - reads X from the user and outputs the result as described above

class Numbers:
  def __init__(self):
    self.n = 0
    self.numbers = []
    self.x = 0

  def read_numbers(self):
    self.n  = int(input("Enter N: "))
    for i in range(self.n):
      m = int(input(f"Enter M number ({i+1}/{self.n}): "))
      self.numbers.append(m)

  def find_x(self):
    self.x = int(input("Enter X: "))
    if self.x in self.numbers:
      print(self.numbers.index(self.x) + 1)
    else:
      print(-1)