from string import ascii_letters

class Children:
    LETRUS = 'qwertyuiopasdfg!@#$'
    LETRUSUP = LETRUS.upper()
    def __init__(self, fio, age, ps, weight):
        self.ferify_name(fio)
        self.ferify_age(age)
        self.__name= fio.split()
        self.__age = age
        #self.name= fio.split()
        #self.age = age
        self.__pasport = ps 
        self.__weight = weight
    @classmethod
    def ferify_name(cls, fio):
        if type(fio) != str:
            raise TypeError("input must be only in letters")
        
        f = fio.split()
        if len(f) != 3 :
            raise TypeError("must have name surname and fathername")
        
        letters = ascii_letters + cls.LETRUS + cls.LETRUSUP
        for s in f :
            if len(s.strip(letters)) !=0 :
                raise TypeError("Imposible sign")
            if len(s) <1  :
                raise TypeError("fio must include something")
    @classmethod
    def ferify_age (cls,age ):
        if type(age) != int or age >100 or age <4:
            raise TypeError("retype age")    
        
    @property
    def get_name(self):
        return self.__name     
    @get_name.setter
    def set_name(self, new_name):
        self.ferify_name(new_name)
        self.__name= new_name
    @property
    def get_age(self):
        return self.__age     
    @get_age.setter
    def set_age(self, new_age):
        self.ferify_age(new_age)
        self.__age= new_age


p = Children("loli sksk eeg ",8,"3exxesxsa",15)
p.set_age= 26
p.set_name= "dori rori ewi"
print(p.__dict__)

