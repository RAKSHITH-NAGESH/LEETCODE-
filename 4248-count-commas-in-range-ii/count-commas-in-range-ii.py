class Solution:
    def countCommas(self, n):
        total = 0

        if n >= 1000:
            total += min(n, 999999) - 1000 + 1

        if n >= 1000000:
            total += (min(n, 999999999) - 1000000 + 1) * 2

        if n >= 1000000000:
            total += (min(n, 999999999999) - 1000000000 + 1) * 3

        if n >= 1000000000000:
            total += (min(n, 999999999999999) - 1000000000000 + 1) * 4

        if n >= 1000000000000000:
            total += (n - 1000000000000000 + 1) * 5

        return total