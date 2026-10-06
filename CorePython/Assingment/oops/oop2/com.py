# sqr=[]
# for i in range(1,21):
#     sqr.append(i*i)
# print(sqr)
# sqr=[i*i for i in range(1,21)]
# print(sqr)
# start=int(input("enter the  starting number  "))
# end=int(input("enter the  Ending number  "))
# alt=[]
# for i in range(start,end+1,2):
#     alt.append(i)
# print(alt)
# alt=[i for i in range(start,end+1,2)]
# print(alt)
# start = int(input("Enter the start Number: "))
# end = int(input("Enter the end Number: "))
# odd=[]
# for i in range(start, end+1):
#     if i % 2 != 0:
#         # print (i)
#         odd.append(i)
# print(odd)
# odd = [i for i in range(start, end+1) if i % 2 != 0]
# print(odd)
sqr={i:i*i for i in range(1,9)}
print(sqr)