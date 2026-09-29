class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        if grid[0][0] != "(" or grid[m - 1][n - 1] != ")":
            return False

        memo = {}

        def dfs(r, c, balance):
            if grid[r][c] == "(":
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False

            remaining = (m - 1 - r) + (n - 1 - c)

            if balance > remaining:
                return False

            if r == m - 1 and c == n - 1:
                return balance == 0

            state = (r, c, balance)

            if state in memo:
                return memo[state]

            if r + 1 < m:
                if dfs(r + 1, c, balance):
                    memo[state] = True
                    return True

            if c + 1 < n:
                if dfs(r, c + 1, balance):
                    memo[state] = True
                    return True

            memo[state] = False
            return False

        return dfs(0, 0, 0)