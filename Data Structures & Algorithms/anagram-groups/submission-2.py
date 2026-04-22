class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = dict()

        for word in strs:
            sorted_word = "".join(sorted(word))
            
            anagram_group = anagram_map.get(sorted_word, [])
            anagram_group.append(word)
            
            anagram_map[sorted_word] = anagram_group
        
        anagram_groups = list(anagram_map.values())

        return anagram_groups