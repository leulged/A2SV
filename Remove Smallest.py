t = int(input())
for _ in range(t):
    n = int(input())
    ls = list(map(int, input().split()))
    ls=list(set(ls))
    ls.sort()
    l=0
    if len(ls)>1:
        for i in range(len(ls)-1):
            if ls[i+1]-ls[i]>1:
                l+=1


    if l>0:
        print("NO")
    else:
        print("YES")
