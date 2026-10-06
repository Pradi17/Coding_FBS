# str = input("Enter a string: ")
# rev = ""
# for ch in str:
#     rev = ch + rev
# print("Reversed string:", rev)
# if rev==str:
#     print("String is Palindrome")
# else:
#     print("String is not palindrome ")


# s = input("Enter a string: ")
# rev = ""
# for i in range(len(s) - 1, -1, -1):
#     rev += s[i]
# print("Reversed string:", rev)




# str = "I am good in coding"
# s = str.split()
# print(s)
# print(type(s))
# for i in range(len(s)-1,-1,-1):
#     print(s[i],end=" ")


# str = 'I am good in coding'
# word = ''
# rev = ''
# for i in str:
#     if i != " ":
#         word = word + i
#     else:
#         if rev == '':
#             rev = word
#         else:
#             rev = word + " " + rev
#         word = ""
# if rev == '':
#     rev = word
# else:
#     rev = word + " " + rev
# print(rev)


import math
path="WNEENSENNN"
x=0
y=0
for ch in path:
    if ch=='N':
        y+=1
    elif ch=='S':
        y-=1
    elif ch=="E":
        x+=1
    elif ch=="W":
        x-=1
# print(4**0.5)

# dist=(x**2 +y**2)**0.5
dist=math.sqrt(x**2 +y**2)

print(f"The distence travled by the person in {path}= {dist}")
    
        
    