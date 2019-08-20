from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target == nums[i] + nums[j]:
                return [i,j]

# 双指针法
def twoSum2(nums: List[int], target: int) -> List[int]:
    # sort first
    sorted_id = sorted(range(len(nums)), key= lambda k: nums[k])
    l = 0
    r = len(nums)-1
    while(l < r):
        if nums[sorted_id[l]] + nums[sorted_id[r]] ==target:
            return [l, r]
        if nums[sorted_id[l]] + nums[sorted_id[r]] < target:
            l += 1
        else:
            r -=1
    return [sorted_id[l], sorted_id[r]]

#  时间复杂度最低
def twoSum3(nums, target):
    hashmap = {}
    for k, v in enumerate(nums):
        other = target - v
        if other in  hashmap:
            return [hashmap[other], k]
        hashmap[v] = k

'''
nums     = [3, 2, 4]
sort_id  = [1, 0, 2]
sort_v   = [2, 3, 4]
'''
nums = [2,3,2,4]
target = 6
res = twoSum3(nums, target)
print(res)