from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        litter = {}
        start = None
        count = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = count
                    count += 1

        target = (1 << count) - 1

        # row, col, collected_mask, energy_left, moves
        q = deque([(start[0], start[1], 0, energy, 0)])

        # best[(row, col, mask)] = maximum energy seen
        best = {(start[0], start[1], 0): energy}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, mask, e, moves = q.popleft()

            if mask == target:
                return moves

            if e == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if classroom[nr][nc] == 'X':
                        continue

                    new_energy = e - 1
                    new_mask = mask

                    if classroom[nr][nc] == 'L':
                        new_mask |= 1 << litter[(nr, nc)]

                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_mask)

                    if best.get(state, -1) >= new_energy:
                        continue

                    best[state] = new_energy
                    q.append((nr, nc, new_mask, new_energy, moves + 1))

        return -1