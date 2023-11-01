import json


class Person:
  def __init__(self, name, weight):
    self.name = name
    self.weight = weight

  def eat(self):
    self.weight += 1
    print("Toi map len roi. {}".format(self.weight))

  def work(self):
    self.weight -= 1
    print("Toi giam can roi {}".format(self.weight))

  def walk(self):
    self.weight -= 1
    print("Toi giam can roi {}".format(self.weight))

  def showInfo(self):
    return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)