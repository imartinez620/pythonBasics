class Cars:
  def __init__(self, name):
    self._name = name


  @property
  def name(self):
    return self._name


  @name.setter
  def name(self, name):
    self._name = name


my_car = Cars("Toyota")
print(my_car._name)

my_car.name = "Renault"
print(my_car._name)
