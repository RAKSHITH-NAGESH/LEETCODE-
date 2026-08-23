class Solution:
    def sumGame(self, num):
        n = len(num) // 2

        left = sum(int(x) for x in num[:n] if x != '?')
        right = sum(int(x) for x in num[n:] if x != '?')

        lq = num[:n].count('?')
        rq = num[n:].count('?')

        if (lq + rq) % 2:
            return True

        return left - right != 9 * (rq - lq) // 2