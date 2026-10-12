class Solution:
    def getPermutation(self, n, k):
        nums = list(range(1, n + 1))
        k -= 1
        result = []

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        while nums:
            index = k // fact[len(nums) - 1]
            result.append(str(nums.pop(index)))
            k %= fact[len(nums)]

        return "".join(result)