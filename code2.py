'''HUNTER 2 largest number'''
a=int(input())
b1=[int(a) for a in input().split()]
b1.sort()
b1.reverse()
for i in range(len(b1)):
    print(b1[i],end="")
