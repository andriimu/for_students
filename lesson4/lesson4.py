
class Mynumber:
    
    @classmethod
    def cheking_validation(cls, x):
        if not isinstance(x, (int,Mynumber)):
            raise TypeError("Non oficial input")
    
    def __init__(self, x):
        self.cheking_validation(x)
        self.x=x
    
    
    def __add__(self,other):
        #self.cheking_validation(other)
        st = other
        if isinstance(other, Mynumber):
            st = other.x
        return Mynumber(self.x + st)
    
t1= Mynumber(6)
t2 = Mynumber(4)

print(t1+3)