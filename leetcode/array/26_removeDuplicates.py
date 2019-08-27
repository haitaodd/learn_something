from typing import List


# 双指针法，快指针用于迭代列表 慢指针用于统计不同元素个数，同时通过移动index 达到删除元素的作用
def removeDuplicates(nums: List[int]) -> int:
    flag = 0
    for e in nums:
        if nums[flag] != e:
            flag += 1
            nums[flag] = e
    return len(nums) and flag + 1


def removeDuplicates2(nums: List[int]) -> int:
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] == nums[i + 1]:
            nums.pop(i + 1)
    return len(nums)


l = [1, 1, 1, 2, 3, 4]
k = [1, 1, 1, 2, 3, 4]
print(removeDuplicates(l))
print(l)

print(removeDuplicates2(k))
print(k)
