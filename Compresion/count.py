# li=[10,20,10,34,20,1]
# vis=[]
# for i in li:
#     if i not in vis:
#         count=0
#     for j in li:
#         if i==j:
#             count+=1
#     print(f"count of {i} = {count}")
from pradipexp import  PradipExc
try :
    no=input("Enter the no " )
    if no!='c':
         raise Exception("I am out of range")
except  Exception as e:
    print(e)