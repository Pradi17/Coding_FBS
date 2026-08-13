# def demo(n):
#     for i in range(1,11):
#         yield i
# g=demo(11)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# g=(i for i in range(5))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

import sys

lst=[i for i in range(100000)]

gen=(i for i in range(100000))

print(sys.getsizeof(lst))
print(sys.getsizeof(gen))