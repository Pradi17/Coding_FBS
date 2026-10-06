# # list 
# li=[7,18,1,33,45,69]
# print(li)
# print(id(li))
# li[5]=7
# print(id(li[0]))
# print(id(li[5]))
# print(li)
# print(id(li))

# li=[12,43,2,90,45,18,7]
# # print(li[2::2])
# # print(li[:-3])
# print(li[-2:])

# Find the Sum of altrnate number in the list

li=[12,43,2,90,45,18,7]
sum=0
for i in range(0,len(li)+1,2):
       sum+=li[i]
print(sum)