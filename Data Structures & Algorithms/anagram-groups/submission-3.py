class Solution:
    def computeKey(self, word) -> str:
        key = [0] * 26
        for letter in word:
            pos = ord(letter) - 97
            key[pos] += 1
        return str(key)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()
        
        for word in strs:
            key = self.computeKey(word)
            
            anagram_group = anagram_map.get(key, [])
            anagram_group.append(word)
            
            anagram_map[key] = anagram_group
        
        anagram_groups = list(anagram_map.values())

        return anagram_groups