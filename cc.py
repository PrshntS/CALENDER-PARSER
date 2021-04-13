t=int(input())
while(t):
    a=input()
    l=a.split('0')
    print(len(l)-l.count(''))
    t=t-1