class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        points1 = []
        points2 = []

        # Store positions of all 1s
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    points1.append((i, j))

                if img2[i][j] == 1:
                    points2.append((i, j))

        shifts = {}

        # Find how many 1s match for every possible shift
        for x1, y1 in points1:
            for x2, y2 in points2:
                shift = (x2 - x1, y2 - y1)

                if shift not in shifts:
                    shifts[shift] = 0

                shifts[shift] += 1

        if not shifts:
            return 0

        return max(shifts.values())     