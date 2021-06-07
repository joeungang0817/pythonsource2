nums = input().split()
nums2 = []
for i in range(len(nums)):
    nums2.append(int(nums[i]))
nums3 = sorted(nums2)
if nums3==nums2:
    print('정상')
else: 
    print('비정상')