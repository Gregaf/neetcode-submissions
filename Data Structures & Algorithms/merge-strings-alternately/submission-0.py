class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        len_word1 = len(word1)
        len_word2 = len(word2)

        for i in range(len_word1):
            res += word1[i]

            if i < len_word2:
                res += word2[i]

        if len_word2 > len_word1:
            res += word2[len_word1:]

        return res