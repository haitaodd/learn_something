from typing import List

'''
双指针：
1。两指针，一头一尾，中间靠拢移动
2。移动的情况下，宽度肯定会减1，寄希望与替换高度较小的板子
3。一个中间变量存储容积，遍历结束后，得到最大的容积
'''


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            tmp = (right - left) * min(height[left], height[right])
            if tmp > max:
                max = tmp
        return max


if __name__ == '__main__':
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    t = Solution()
    res = t.maxArea(nums)

    print(res)
