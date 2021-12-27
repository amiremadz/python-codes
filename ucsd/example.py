class Geek:
    def __init__(self, age = 0):
         self._age = age
      
    # getter method
    def get_age(self):
        return self._age
      
    # setter method
    def set_age(self, x):
        self._age = x

    def del_age(self):
         del self._age
     
raj = Geek()
  
raj.set_age(21)
print(raj.get_age())
print(raj._age)

raj.del_age()

class Geek:
    def __init__(self, age = 0):
         self._age = age
      
    @property    
    def age(self):
        return self._age
      
    @age.setter
    def age(self, x):
        self._age = x
 
    @age.deleter
    def age(self):
        del self._age

    def __len__(self):
        return 0

raj = Geek()

len(raj)


raj.age = 25
#raj.age(25)


print('age is:', raj.age)
del(raj.age)
print(raj.age)


