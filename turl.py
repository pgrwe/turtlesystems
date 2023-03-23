import turtle
class LSystem:
  def __init__(self, angle, iterations, distance):
    self.angle = angle
    self.iters = iterations
    self.distance = distance
    self.axiom = "FX"
    self.result = self.axiom


  def processString(self, old):
    new_str = ""
    for ch in old:
      if ch == 'X':
        new_str += 'X+YF'
      elif ch == 'Y':
        new_str += 'FX-Y'
      else:
        new_str += ch
    return new_str


  def generateInstructions(self):
    for i in range(self.iters):
      self.result = self.processString(self.result)

  def visualize(self):
    pen = turtle.Turtle()
    wn = turtle.Screen()

    for ch in self.result:
      if ch == 'F':
        pen.forward(self.distance)
      elif ch == '-':
        pen.left(self.angle)
      elif ch == '+':
        pen.right(self.angle)
    wn.exitonclick()



def main():
  angle = int(input("Pleae enter an angle: "))
  iters = int(input("Pleae enter a number of iterations: "))
  dist = int(input("Pleae enter a distance: "))

  lsys = LSystem(angle, iters, dist)
  lsys.generateInstructions()
  print(lsys)
  lsys.visualize()

main()