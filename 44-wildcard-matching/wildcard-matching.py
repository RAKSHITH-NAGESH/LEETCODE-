class Solution:
    def isMatch(self, s, p):

        dp = [False] * (len(p) + 1)
        dp[0] = True

        # Empty string matched with pattern containing only '*'
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 1]
            else:
                break

        for i in range(1, len(s) + 1):

            new_dp = [False] * (len(p) + 1)

            for j in range(1, len(p) + 1):

                if p[j - 1] == '*':
                    # '*' matches empty OR one/more characters
                    new_dp[j] = new_dp[j - 1] or dp[j]

                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    new_dp[j] = dp[j - 1]

            dp = new_dp

        return dp[len(p)]