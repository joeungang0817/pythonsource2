nums = input().split()
nums2 = []
for i in range(len(nums)):
    nums2.append(int(nums[i]))
nums2.sort()
for x in nums2:
    print(x,end=' ')