li=[18,7,45,13,1]
print(f"Before Swaping= {li}")
for i in range(len(li)-1):
    minindex=i
    for j in range(i+1,len(li)):
        if li[j]<li[minindex]:
            minindex=j
    li[i],li[minindex]=li[minindex],li[i]
print(f"After Swaping= {li}")