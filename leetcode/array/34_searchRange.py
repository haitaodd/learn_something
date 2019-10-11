from typing import List

'''
二分查找：
   首先要排序
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left_range(nums, target):
            st, end = 0, len(nums) - 1
            while st < end:
                mid = st + (end - st) // 2
                if nums[mid] < target:
                    st = mid + 1  # 持续逼近
                else:
                    end = mid
            return st if nums and nums[st] == target else -1

        def find_right_range(nums, target):
            st, end = 0, len(nums) - 1
            while st < end:
                mid = st + (end - st) // 2 + 1  # 右边界
                if nums[mid] > target:
                    end = mid - 1  # 持续逼近
                else:
                    st = mid
            return st if nums and nums[st] == target else -1

        return [find_left_range(nums, target), find_right_range(nums, target)]

    def searchRange2(self, nums, target):
            if not nums: return [-1 , -1]
            res = []
            low, high = 0, len(nums) - 1
            while low < high:
                mid = low + (high - low) // 2
                if nums[mid] > target or target == nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            if nums[low] != target:
                return [-1,-1]
            res.append(low)
            high = len(nums) - 1
            while low < high:
                mid = low + (high - low) // 2 + 1
                if nums[mid] < target or target == nums[mid]:
                    low = mid
                else:
                    high = mid - 1
            res.append(high)
            return  res

    def searchRange3(self, nums: List[int], target: int) -> List[int]:
        res = []
        for e, value in enumerate(nums):
            if value == target:
                res.append(e)
        if res:
            return [res[0], res[-1]]
        else:
            return [-1, -1]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    t = Solution()

    res = t.searchRange2([], 0)
    print(res)
