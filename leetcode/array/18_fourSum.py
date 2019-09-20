from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        len_num = len(nums)
        res = []
        nums.sort()
        for i in range(len_num - 3):
            target_i = target - nums[i]
            #!!! skip duplicate element
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i + 1, len_num - 2):
                # !!!skip duplicate element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len_num - 1
                while left < right:
                    t_sum = nums[left] + nums[right] + nums[j]
                    if t_sum == target_i:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # skip duplicate elements
                        while (left < right and nums[left + 1] == nums[left]): left += 1
                        while (left < right and nums[right - 1] == nums[right]): right -= 1

                        left += 1
                        right -= 1
                    elif t_sum < target_i:
                        left += 1
                    else:
                        right -= 1
        return res


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    nums2 = [-3, -2, -1, 0, 0, 1, 2, 3]
    nums3 = [-1, -5, -5, -3, 2, 5, 0, 4]

    a = nums3
    target = 0
    target3 = -7
    res = Solution().fourSum(nums3, target3)

    if a == nums2:
        print(res)
        assert res == [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2],
                       [-2, 0, 0, 2], [-1, 0, 0, 1]]
    elif a == nums:
        print(res)
    elif a == nums3:
        print(res)
        assert res == [[-5, -5, -1, 4], [-5, -3, -1, 2]]
