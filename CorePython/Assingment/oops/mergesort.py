def conqure(li,start,mid,end):
    tem=[]
    left=start
    right=mid+1
    while left<=mid and right <=end:
        if li[left]<li[right]:
            tem.append(li[left])
            left+=1
        else:
            tem.append(li[right])
            right+=1
    while left<=mid:
        tem.append(li[left])
        left+=1
    while right<=end:
        tem.append(li[right])
        right+=1
    k=start
    for x in tem:
        li[k]=x
        k=k+1
        
def divide(li,start,end,):
    if start<end:
        mid=(start+end)//2
        divide(li,start,mid)
        divide(li,mid+1,end)
        conqure(li,start,mid,end)     
li=[7,1,18,33,69,12]
print(f"Before Sorting{li} ")
divide(li,0,len(li)-1)
print(f"After Sorting {li}")


# WAP to reverse the list in same list
l = [10, 20, 30, 40, 50]
left = 0
rigth = len(l) - 1
while left< rigth:
    l[left], l[rigth] = l[rigth], l[left]
    left += 1
    rigth -= 1
print(l)