# 双指针+分治
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        res = []
        if nums_len < 3:
            return res
        nums.sort()
        for i in range(nums_len):
            if nums[i] > 0: return res
            if i > 0 and (nums[i] == nums[i - 1]):
                continue

            left = i + 1
            right = nums_len - 1

            while left < right:
                t_sum = nums[left] + nums[right] + nums[i]
                if t_sum == 0:
                    res.append([nums[left], nums[right], nums[i]])

                    # skip duplicate element
                    while (left < right) and nums[left + 1] == nums[left]: left += 1
                    while (left < right) and nums[right - 1] == nums[right]: right -= 1

                    left += 1
                    right -= 1
                elif t_sum < 0:
                    left += 1
                else:
                    right -= 1

        return res


if __name__ == '__main__':
    a = [-1, 0, 1, 2, -1, -4]
    b = [-2, 0, 1, 1, 2]
    res = Solution().threeSum(b)
    print(res)
