import sys

# alg solution:
# start with random team with largest size
# find best set of pizzas for that team
# move on to next biggest team
# repeat until all teams done


class Team:
  def __init__(self, size):
    self.size = size
    self.num_pizzas = 0
    self.pizzas = []
  
  def add_pizza(self, pizza):
    self.pizzas.append(pizza)
    self.num_pizzas += 1

class Pizza:
  def __init__(self, index, num_ingredients, ingredients):
    self.index = index
    self.num_ingredients = num_ingredients
    self.ingredients = ingredients

class Solution:
  def __init__(self):
    self.num_pizzas = 0
    self.num_doub_teams = 0
    self.num_tri_teams = 0
    self.num_quad_teams = 0
    self.pizzas = []
    self.output = "Hello world!"
  
  def read(self):
    # open file for reading
    filename = str(sys.argv[1])
    with open(filename) as fd:
      
      # read in first line, general info
      lines = fd.read().split('\n')
      n = [int(x) for x in lines[0].split()]
      self.num_pizzas = n[0]
      self.num_doub_teams = n[1]
      self.num_tri_teams = n[2]
      self.num_quad_teams = n[3]

      # read in pizzas
      for i, l in enumerate(lines[1:]):
        line = l.split()
        if line == []:
          break
        pizza = Pizza(i, int(line[0]), line[1:])
        self.pizzas.append(pizza)

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
  sol.read()
  print(sol)
  sol.run()