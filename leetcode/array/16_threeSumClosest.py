from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        min = nums[0] + nums[1] + nums[2]
        if nums_len < 3: return 0
        nums.sort()

        for i in range(nums_len - 2):
            left = i + 1
            right = nums_len - 1

            while left < right:
                t_sum = nums[left] + nums[right] + nums[i]
                if abs(target - t_sum) < abs(target - min):
                    min = t_sum
                if t_sum == target:
                    return target
                elif nums[left] + nums[right] + nums[i] < target:
                    left += 1
                else:
                    right -= 1
        return min


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    res = Solution().threeSumClosest(nums, target)
    print(res)
