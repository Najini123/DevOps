class Animal:
    def __init__(self,name,age):
      self.name=name
      self.age=age
    def display(self):
      pass
class carnivores(Animal):
    def __init__(self,name,age,shout):
      self.shout=shout
      super.__init__(name,age)
    def display(self):
        pass
    
a=Animal()
print(a.display())
a=carnivores("buddy",20,"bow",)
print(a.display())
