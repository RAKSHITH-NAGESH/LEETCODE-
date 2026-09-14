class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        need = {}

        for word in words:
            need[word] = need.get(word, 0) + 1

        answer = []

        for start in range(word_len):
            left = start
            right = start
            count = 0
            window = {}

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in need:
                    window[word] = window.get(word, 0) + 1
                    count += 1

                    while window[word] > need[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        answer.append(left)

                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    window = {}
                    count = 0
                    left = right

        return answer