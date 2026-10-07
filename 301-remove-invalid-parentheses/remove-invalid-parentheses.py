class Solution:
    def removeInvalidParentheses(self, s):
        result = []
        visited = set()

        def isValid(text):
            balance = 0

            for ch in text:
                if ch == "(":
                    balance += 1
                elif ch == ")":
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        def backtrack(index, left, right, balance, path):
            if balance < 0:
                return

            if index == len(s):
                if left == 0 and right == 0 and balance == 0:
                    result.append("".join(path))
                return

            state = (index, left, right, balance, "".join(path))

            if state in visited:
                return

            visited.add(state)

            ch = s[index]

            if ch == "(":
                if left > 0:
                    backtrack(index + 1, left - 1, right, balance, path)

                path.append(ch)
                backtrack(index + 1, left, right, balance + 1, path)
                path.pop()

            elif ch == ")":
                if right > 0:
                    backtrack(index + 1, left, right - 1, balance, path)

                if balance > 0:
                    path.append(ch)
                    backtrack(index + 1, left, right, balance - 1, path)
                    path.pop()

            else:
                path.append(ch)
                backtrack(index + 1, left, right, balance, path)
                path.pop()

        left = 0
        right = 0

        for ch in s:
            if ch == "(":
                left += 1
            elif ch == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1

        backtrack(0, left, right, 0, [])

        return list(set(result))