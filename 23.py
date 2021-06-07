avg = input().split()
avgcal = []
for i in range(3):
    avgcal.append(int(avg[i]))
avgfin = (avgcal[0]+avgcal[1]+avgcal[2])/3
print(int(avgfin))
