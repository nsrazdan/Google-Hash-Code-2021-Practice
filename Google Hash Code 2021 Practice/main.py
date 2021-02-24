import sys

class Pizza:
  def __init__(self, num_ingredients):
    self.num_ingredients = num_ingredients
    self.ingredients = [];

class Solution:
  def __init__(self):
    self.num_pizzas = 0
    self.num_doub_teams = 0
    self.num_tri_teams = 0
    self.num_quad_teams = 0
    self.output = "Hello world!"
  
  def read(self):
    filename = str(sys.argv[0])

  def solve(self):
    x = None

  def display(self):
    print(self.output)

  def run(self):
    self.read()
    self.solve()
    self.display()


if __name__ == "__main__":
  sol = Solution()
  sol.run()