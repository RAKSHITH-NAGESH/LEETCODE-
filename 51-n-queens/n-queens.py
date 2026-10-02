class Solution:
    def solveNQueens(self, n):
        result = []

        board = [["."] * n for _ in range(n)]

        columns = set()
        diagonal1 = set()
        diagonal2 = set()

        def backtrack(row):
            if row == n:
                solution = []

                for i in range(n):
                    solution.append("".join(board[i]))

                result.append(solution)
                return

            for col in range(n):

                # Check column
                if col in columns:
                    continue

                # Check main diagonal
                if row - col in diagonal1:
                    continue

                # Check other diagonal
                if row + col in diagonal2:
                    continue

                # Place queen
                board[row][col] = "Q"
                columns.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)

                # Move to next row
                backtrack(row + 1)

                # Remove queen
                board[row][col] = "."
                columns.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

        backtrack(0)

        return result