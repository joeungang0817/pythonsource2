nums = input().split()
list1 = []
for i in range(2):
    list1.append(int(nums[i]))

print(type(list1))
listshare = list1[0]/list1[1]
listshare2 = list1[0]%list1[1]
print(int(listshare), listshare2)