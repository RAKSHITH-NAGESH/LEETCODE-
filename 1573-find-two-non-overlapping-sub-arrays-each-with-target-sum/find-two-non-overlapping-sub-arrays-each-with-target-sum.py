class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)

        best = [float('inf')] * n

        left = 0
        total = 0
        answer = float('inf')

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                # Previous valid subarray before current one
                if left > 0 and best[left - 1] != float('inf'):
                    answer = min(answer, length + best[left - 1])

                # Store the shortest valid subarray found so far
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)
            else:
                if right > 0:
                    best[right] = best[right - 1]

        if answer == float('inf'):
            return -1

        return answer