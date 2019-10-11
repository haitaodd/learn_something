class Solution:
    def longestPalindrome(self, s: str) -> str:

        pass

    # 暴力解法
    def longestPalindrome1(self, s):
        slen = len(s)
        if slen < 2: return s
        longest = ''
        for i in range(len(s)):
            for j in range(i+1 , len(s)+1):
                sub_str = s[i:j]
                if sub_str[::-1] == sub_str and len(sub_str) > len(longest):
                    longest = sub_str
        return longest

    # 动态规划
    def longestPalindrome2(self, s: str) -> str:
        pass

    # 马拉车算法
    def longestPalindrome3(self, s: str) -> str:
        pass
    def longestPalindrome4(self, s: str) -> str:
        
        pass

if __name__ == '__main__':
    t = Solution()
    s = "babad"
    s2 = 'cc'
    res = t.longestPalindrome1(s)

    print(res)
