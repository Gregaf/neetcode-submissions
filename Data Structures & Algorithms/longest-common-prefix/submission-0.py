class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        word_first = strs[0]

        for i in range(len(word_first)):
            for word in strs[1:]:
                if i >= len(word) or word[i] != word_first[i]:
                    return res

            res += word_first[i]

        return res