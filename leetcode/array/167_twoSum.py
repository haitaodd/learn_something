
# 超时了，N^2 弱爆了
def twoSum(numbers, target):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]


# 双指针法
def twoSum2(numbers, target):
    l=0
    r = len(numbers)-1
    while (l < r):
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        if numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1
    return [l+1, r+1]

alist = [2, 7, 14, 15]
tar = 21
print(twoSum(alist, tar))