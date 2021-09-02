class Solution:
    def twoSum(self, num, target):
        ls = []
        for i in range(0, len(num)):
            item = target - num[i]
            num[i] = "done"
            if item in num:
                if i != num.index(item):
                    ls.append(i)
                    ls.append(num.index(item))
                    return ls
