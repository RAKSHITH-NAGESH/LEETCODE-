class Solution:
    def maxNumOfSubstrings(self, s):
        first = {}
        last = {}

        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i
            last[s[i]] = i

        intervals = []

        for c in first:
            left = first[c]
            right = last[c]

            i = left
            valid = True

            while i <= right:
                ch = s[i]

                if first[ch] < left:
                    valid = False
                    break

                right = max(right, last[ch])
                i += 1

            if valid:
                intervals.append((left, right))

        intervals.sort(key=lambda x: x[1])

        answer = []
        end = -1

        for left, right in intervals:
            if left > end:
                answer.append(s[left:right + 1])
                end = right

        return answer