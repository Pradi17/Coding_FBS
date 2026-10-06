class Time:
    def __init__(self,h,m,sec):
        self.h=h
        self.m=m
        self.sec=sec
    def __str__(self):
        return f"{self.h} : {self.m} :{self.sec}"
    def __add__(self, other):
        sec=self.sec+other.sec
        carry=sec//60
        sec=sec%60
        print(carry,sec)
        min=self.m+other.m+carry
        carry=min//60
        min=min%60
        print(carry,min)
        h=self.h+other.h+carry
        return Time(h,min,sec)
        # return f"{self.h+other.h} :{self.m +other.m} :{self.sec +other.sec}"
    # def __sub__(self, other):
    #     return f"{self.h-other.h} :{self.m -other.m} :{self.sec -other.sec}"
        
        
        
t1=Time(12,22,30)
t2=Time(12,33,60)
print(t1)
print(t2)
print(t1+t2)
