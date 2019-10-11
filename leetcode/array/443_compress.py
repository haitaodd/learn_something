from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write

    def compress2(self, chars: List[str]) -> int:
        slow = count = 0
        for fast, c in enumerate(chars):
            if fast + 1 == len(chars) or chars[fast + 1] != c:
                chars[count] = c
                count += 1
                if fast > slow:
                    for i in str(fast - slow + 1):
                        chars[count] = i
                        count += 1
                slow = fast + 1
        return count


if __name__ == '__main__':
    nums = ["a", "a", "b", "b", "c", "c", "c"]
    nums3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]

    t = Solution()
    res = t.compress2(nums3)

    print(res, nums3)
