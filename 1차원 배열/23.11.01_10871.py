i,j = input().split()
k = list(map(int,input().split(' ')))
l = []
for n in k:
    if int(n) < int(j) :
        l.append(str(n))
print(' '.join(l))
