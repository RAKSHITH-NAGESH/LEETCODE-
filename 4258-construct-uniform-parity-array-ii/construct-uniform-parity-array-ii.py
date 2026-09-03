class Solution:
    def uniformArray(self, nums1):
        return all(x % 2 == 0 for x in nums1) or min(nums1) % 2 == 1