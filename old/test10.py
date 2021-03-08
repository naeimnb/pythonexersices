a = int(input())
HowManyMatch = [int(x) for x in input().split()]
if a == len(HowManyMatch):
    count = 0
for i in HowManyMatch:
    if i < 3 :
        count+=1
        d = count//3
print(d)