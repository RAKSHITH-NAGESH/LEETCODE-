class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)

        # best_start[end] = largest starting index of a
        # palindrome ending at 'end' with length at least k
        best_start = [-1] * n

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1

                if length >= k:
                    best_start[right] = max(best_start[right], left)

                left -= 1
                right += 1

        # Generate all palindromes
        for i in range(n):
            # Odd length palindromes
            expand(i, i)

            # Even length palindromes
            expand(i, i + 1)

        # Greedily choose the palindrome that ends earliest
        answer = 0
        last_end = -1

        for end in range(n):
            if best_start[end] > last_end:
                answer += 1
                last_end = end

        return answer