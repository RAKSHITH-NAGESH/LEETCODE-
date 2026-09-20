class Solution:
    def reverseDegree(self, s):
        answer = 0

        for i in range(len(s)):
            alphabet_position = ord(s[i]) - ord('a') + 1
            reverse_position = 27 - alphabet_position

            answer += reverse_position * (i + 1)

        return answer