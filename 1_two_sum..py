def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        if target - nums[i] in nums and i != nums.index(target - nums[i]):
            return [i, nums.index(target - nums[i])]


num = [2, 7, 11, 15]
target1 = 9
print(twoSum(num, target1))
