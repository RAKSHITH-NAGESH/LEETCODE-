class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        diffs.sort(reverse=True)
        diffs.append(0)

        for i in range(len(diffs) - 1):
            needed = (diffs[i] - diffs[i + 1]) * (i + 1)

            if k >= needed:
                k -= needed
            else:
                level = diffs[i] - k // (i + 1)
                remainder = k % (i + 1)

                result = sum(x * x for x in diffs[i + 1:-1])
                result += remainder * (level - 1) ** 2
                result += (i + 1 - remainder) * level ** 2

                return result

        return 0