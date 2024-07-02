class Integer:
    
    @classmethod
    def chek_for_valid(cls, value):
        if type(value) != int:
            raise TypeError("Value must be integer")
        
    
    
    def __set_name__(self, owner, name):
        self.name = "_" + name
    def __get__(self, instance, owner):
        print("returning")
        return getattr(instance,self.name)
    def __set__(self, instance, value):
        self.chek_for_valid(value)
        print("cheked")
        setattr(instance,self.name, value)

class Point:
    x = Integer()
    y = Integer()
    z = Integer()
    def __init__(self,x,y,z):
        self.x = x
        self.y = y 
        self.z = z
  
        
t = Point(3,3,4)
print(t.__dict__)

print(t.z)