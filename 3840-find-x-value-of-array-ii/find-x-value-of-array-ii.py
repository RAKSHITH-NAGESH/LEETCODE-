class Solution:
    def resultArray(self, nums, k, queries):

        n = len(nums)

        # tree[node][r] = number of prefixes
        # whose product % k == r
        tree = [[0] * k for _ in range(4 * n)]

        # tree_prod[node] = product of whole segment % k
        tree_prod = [0] * (4 * n)

        def build(node, left, right):

            if left == right:
                value = nums[left] % k
                tree_prod[node] = value
                tree[node][value] = 1
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            merge(node)

        def merge(node):

            left_node = node * 2
            right_node = node * 2 + 1

            left_product = tree_prod[left_node]
            right_product = tree_prod[right_node]

            tree_prod[node] = (left_product * right_product) % k

            for r in range(k):
                tree[node][r] = 0

            # Prefixes completely inside left part
            for r in range(k):
                tree[node][r] += tree[left_node][r]

            # Prefixes = whole left part + prefix of right part
            for r in range(k):
                new_r = (left_product * r) % k
                tree[node][new_r] += tree[right_node][r]

        def update(node, left, right, index, value):

            if left == right:
                value %= k
                tree_prod[node] = value

                for r in range(k):
                    tree[node][r] = 0

                tree[node][value] = 1
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, right, index, value)

            merge(node)

        def query(node, left, right, start):

            # Entire segment is before start
            if right < start:
                return None

            # Entire segment is inside the required range
            if start <= left:
                return (tree_prod[node], tree[node][:])

            mid = (left + right) // 2

            left_result = query(node * 2, left, mid, start)
            right_result = query(node * 2 + 1, mid + 1, right, start)

            if left_result is None:
                return right_result

            if right_result is None:
                return left_result

            left_product = left_result[0]
            left_prefix = left_result[1]

            right_product = right_result[0]
            right_prefix = right_result[1]

            result_product = (left_product * right_product) % k
            result_prefix = [0] * k

            # Prefixes from left
            for r in range(k):
                result_prefix[r] += left_prefix[r]

            # Whole left + prefix of right
            for r in range(k):
                new_r = (left_product * r) % k
                result_prefix[new_r] += right_prefix[r]

            return (result_product, result_prefix)

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Update persists
            update(1, 0, n - 1, index, value)

            # Get prefix counts from nums[start:]
            result = query(1, 0, n - 1, start)

            answer.append(result[1][x])

        return answer