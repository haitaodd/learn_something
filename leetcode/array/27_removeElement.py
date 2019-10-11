from typing import List
'''
s1:
    1。一个变量存储不同元素，将要存储在list中的位置
    2。遍历list，遇到需要存储的元素，放到指定位置即可
s2:
    1。双指针，两端向中间靠拢
    2。后面目标元素直接过滤掉了（引用向前），
    3。前面碰到目标元素用后面的不同的元素替换
    这种解法，注意 nums=[1] ,val=1的情况
'''

class Solution:
    def removeElement1(self, nums: List[int], val: int) -> int:
        begin = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[begin] = nums[i]
                begin+=1
        return begin

    def removeElement2(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left] == val and nums[right] !=val:
                nums[left] = nums[right]
                nums[right] = val
            if nums[left] != val:
                left +=1
            if nums[right] ==val:
                right -=1
        return  right +1

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    nums2 = [0,1,2,2,3,0,4,2]
    nums3 = [1]
    val = 2
    t = Solution()
    res = t.removeElement1(nums3, 1)
    res2 = t.removeElement2(nums3, 1)

    print(res,res2)
