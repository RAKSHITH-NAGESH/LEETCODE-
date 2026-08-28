class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(s - target) < abs(ans - target):
                    ans = s

                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return s

        return ans