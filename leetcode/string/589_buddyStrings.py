
# 题目比较容易让人误解， 只有移动A字符串的两个字符后，与B相等，才返回true

def buddyStrings(A: str, B: str) -> bool:
    if len(A) != len(B):
        return False
    if len(set(A)) < len(A) and A == B:
        return True
    a = []
    b = []
    for i in range(len(A)):
        if A[i] != B[i]:
            a.append(A[i])
            b.append(B[i])
    if len(a) == len(b)  == 2 and a[::-1] ==b:
        return True
    else:
        return False


A = "ab"
B = "ab"

print(buddyStrings(A, B))
