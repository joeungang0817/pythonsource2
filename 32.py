strin = input()
strin2 = list(strin)
print(strin2)
for i in range(len(strin2)):
    if i>len(strin2):
        break
    print(strin2[i-1],strin2[i])
