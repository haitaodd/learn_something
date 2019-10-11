class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = {}
        i, ans = -1, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i)
            st[s[j]] = j
        return ans


if __name__ == '__main__':
    s = "pwwkew"
    t = Solution()
    res = t.lengthOfLongestSubstring(s)

    print(res)
