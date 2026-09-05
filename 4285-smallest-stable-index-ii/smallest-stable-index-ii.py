class Solution:
    def firstStableIndex(self, nums, k):
        suffix_min = [0] * len(nums)
        suffix_min[-1] = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        prefix_max = nums[0]

        for i in range(len(nums)):
            prefix_max = max(prefix_max, nums[i])

            if prefix_max - suffix_min[i] <= k:
                return i

        return -1