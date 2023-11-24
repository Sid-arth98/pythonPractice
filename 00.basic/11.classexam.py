class parent:
    def __init__(self,name,age,rollnum):
        self.name = name
        self.age  = age
        self.rollnum = rollnum

class child1(parent):
    def __init__(self,name,age,rollnum,score):
        super().__init__(name,age,rollnum)
        self.score = score 
        

    def changescore(self,changedscore):
        self.score=changedscore 
        return self  

sid = child1("sid",25,"n113050",800)
print(sid.changescore(600))
print(f"{sid.age} { sid.name} {sid.rollnum} {sid.score}")