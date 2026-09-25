class Solution:
    def braceExpansionII(self, expression):
        def solve(s):
            result = set()
            current = {""}
            i = 0

            while i < len(s):
                if s[i] == "{":
                    start = i
                    depth = 0

                    while i < len(s):
                        if s[i] == "{":
                            depth += 1
                        elif s[i] == "}":
                            depth -= 1

                        if depth == 0:
                            break

                        i += 1

                    words = solve(s[start + 1:i])

                    current = {
                        a + b
                        for a in current
                        for b in words
                    }

                elif s[i] == ",":
                    result.update(current)
                    current = {""}

                else:
                    current = {
                        word + s[i]
                        for word in current
                    }

                i += 1

            result.update(current)
            return result

        return sorted(solve(expression))