class Solution:
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            digit_sum = 0
            num = nums[i]

            while num > 0:
                digit_sum += num % 10
                num //= 10

            if digit_sum == i:
                return i

        return -1
        