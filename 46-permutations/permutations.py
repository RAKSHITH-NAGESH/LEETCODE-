class Solution:
    def permute(self, nums):
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()

        backtrack([])
        return result