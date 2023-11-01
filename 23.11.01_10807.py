i = int(input())
j = list(map(int, input().split(' ')))
l = int(input())
cnt = 0
for k in j:
    if l == k:
        cnt += 1
print(cnt)