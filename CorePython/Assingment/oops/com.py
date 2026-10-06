# Dikha raha hai.....
# li=[2,3,4,5,6,7,11]
# newl=[]
# for i in li:
#     newl.append(i*i)
# print(f"New list={newl}")    

# [expression loop itrater]
# newli=[i*i for i in li]
# print(f"New List ={newli}")


# li=[36,45,55,65,75]
# print(f"Before Updation=\t {li}")
# updated=[i+10 for i in li]
# # for i in li:
# #     updated.append(i+10)
# print(f"Updated Marks=\t {updated}")
 
# print the Even number in list
# li=[1,13,22,11,5,4,7,8]
# newLi=[i for i in li if i%2==0]
# for i in li:
#     if i%2==0:
#         newLi.append(i)
# print(f"Even nuber= {newLi}")
        
# li=[1,13,22,11,5,4,7,8]
# print(li)
# newLi=["Even" if i%2==0 else "odd" for i in li]
# for i in li:
#     if i%2==0:
#         newLi.append("Even")
#     else:
#         newLi.append("Odd")    
# print(newLi)        

# li=["Blue","Orange","Red","Voilet","Green","HotPink","Hot Red"]
# bag=[i.upper() for i in li if i=="Red" or i=="Orange"]
# # for i in li:
#     # if i=="Red" or i=="Orange":
#     #     bag.append(i.upper())
# print(bag)        
        

dict={"Rahul":122222,"Virat":9230,"Sachin":1000000}
newDict={k:v+100  for k,v in dict.items()}
# for k,v in dict.items():
    # newDict[k]=v+100
print(newDict)    
