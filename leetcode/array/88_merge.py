from typing import List

'''
双指针法：基于nums1 inplace sort，需要单独判断nums2的情况
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p, m, n = m + n - 1, m - 1, n - 1
        while (m >= 0 and n >= 0):
            if nums1[m] > nums2[n]:
                nums1[p] = nums1[m]
                p = p - 1
                m = m - 1
            else:
                nums1[p] = nums2[n]
                p = p - 1
                n = n - 1
        # the inplace sort is base on nums1,
        while (n >= 0):
            nums1[p] = nums2[n]
            p = p - 1
            n = n - 1

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:m + n] = nums2
        nums1.sort()


if __name__ == '__main__':
    t = Solution()
    num1 = [0,0,0,0]
    m = 0
    num2 = [2, 5, 6]
    n = 3
    t.merge(num1, m, num2, n)
    print(num1)

    num11, mm = [0], 0
    num22, nn = [1], 1
    t.merge(num11, mm, num22, nn)
    print(num11)
