"""
滑动窗口+索引计数
s为被搜索的字符， t为必须要要包含的字符
1）将t放入map中，key为字符/value为计数
2）找到条件为 map value都 <=0
3) 滑动窗口，找到的字符串是否为最小

同 443
https://blog.csdn.net/u013115610/article/details/70257445
"""
import sys
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mem = defaultdict(int)
        for char in t:
            mem[char] += 1
        t_len = len(t)
        min_window = sys.maxsize
        minl, minr = 0, 0
        left = 0
        for right, char in enumerate(s):
            if char in mem:
                mem[char] -= 1
                if mem[char] >= 0:
                    t_len -= 1
            while t_len == 0:
                if right - left < min_window:
                    min_window = right-left
                    minl, minr = left, right
                if s[left] in mem:
                    mem[s[left]] += 1
                    if mem[s[left]] > 0:
                        t_len += 1
                left += 1

        return "" if min_window == sys.maxsize else s[minl:minr + 1]


if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'

    s1 = 'a'
    t1 = 'aa'
    c = Solution()
    res = c.minWindow(s1, t1)

    print(res)