class Solution:
    def totalNQueens(self, n):
        columns = set()
        diagonal1 = set()
        diagonal2 = set()

        count = [0]

        def backtrack(row):
            if row == n:
                count[0] += 1
                return

            for col in range(n):
                if col in columns:
                    continue

                if row - col in diagonal1:
                    continue

                if row + col in diagonal2:
                    continue

                columns.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)

                backtrack(row + 1)

                columns.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

        backtrack(0)

        return count[0]