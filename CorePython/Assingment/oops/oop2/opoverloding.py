class Time:
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec} "   
    def __add__(self, other):
        s=self.sec+other.sec
        rem=s//60
        s=s%60
        m=self.min+other.min+rem
        rem=m//60
        m=m%60
        h=self.hr+other.hr+rem
        t=Time(h,m,s)
        return t
t1=Time(3,40,56)
t2=Time(4,50,49)
print(t1+t2)