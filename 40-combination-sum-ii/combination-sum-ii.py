class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()

        result = []

        def backtrack(start, target, current):
            if target == 0:
                result.append(current[:])
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since the array is sorted
                if candidates[i] > target:
                    break

                current.append(candidates[i])

                # i + 1 means each number can be used only once
                backtrack(i + 1, target - candidates[i], current)

                current.pop()

        backtrack(0, target, [])

        return result
