def gen(n):
    for i in range(1,n+1):
        yield(i)
g=gen(5)
print(next(g)) 
print("Ruk jara")
print(next(g))
print("Next no ko aane de")
print(next(g))
print("Mera no aa gaya ")
print(next(g))
print(next(g))
print(next(g))
