def team(x,y):
    d = x[0]>=y[0] and x[1]>=y[1] and x[2]>=y[2]
    e= x[0]>y[0] or x[1]>y[1] or x[2]>y[2]
    return d and e
t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))

    if team(a,b) and team(b,c):
        print('yes')
    elif team(a,c) and team(c,b):
        print('yes')
    elif team(b,a) and team(a,c):
        print('yes')
    elif team(b,c) and team(c,a):
        print('yes')
    elif team(c,a) and team(a,b):
        print('yes')
    elif team(c,b) and team(b,a):
        print('yes')
    else:
        print('no')