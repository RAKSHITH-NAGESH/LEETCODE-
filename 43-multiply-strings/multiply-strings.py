class Solution:
    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):

                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')

                product = a * b

                position = i + j + 1
                carry_position = i + j

                result[position] += product

                result[carry_position] += result[position] // 10
                result[position] %= 10

        # Remove leading zeros
        start = 0

        while start < len(result) - 1 and result[start] == 0:
            start += 1

        answer = ""

        for i in range(start, len(result)):
            answer += str(result[i])

        return answer