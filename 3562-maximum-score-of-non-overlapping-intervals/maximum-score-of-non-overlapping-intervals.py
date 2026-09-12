class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = []

        for i in range(n):
            l, r, w = intervals[i]
            arr.append((l, r, w, i))

        arr.sort()

        starts = [x[0] for x in arr]

        def find_next(r):
            left = 0
            right = n

            while left < right:
                mid = (left + right) // 2

                if starts[mid] <= r:
                    left = mid + 1
                else:
                    right = mid

            return left

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, index = arr[i]
            nxt = find_next(r)

            for k in range(1, 5):

                # Skip current interval
                skip_score, skip_list = dp[i + 1][k]

                # Take current interval
                next_score, next_list = dp[nxt][k - 1]

                take_score = w + next_score
                take_list = [index] + next_list

                # Keep indices sorted for lexicographical comparison
                take_list.sort()

                if take_score > skip_score:
                    dp[i][k] = (take_score, take_list)

                elif take_score < skip_score:
                    dp[i][k] = (skip_score, skip_list)

                else:
                    if take_list < skip_list:
                        dp[i][k] = (take_score, take_list)
                    else:
                        dp[i][k] = (skip_score, skip_list)

        return dp[0][4][1]