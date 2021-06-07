num = int(input())
sum=0
plus=1
for x in range(0,num,2):
    for i in range(0,sum+plus):
        print('*',end='')
    print()
    sum+=1
    plus+=1