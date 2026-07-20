class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # identify anagram: sort, count characters
        # use bucket as key, create string from list?

        anagram_group_map = dict()
        for word in strs:
            key = [0] * 26
            for char in word:
                char_index = ord(char) - ord('a')
                key[char_index] += 1
            
            hashable_key = tuple(key)
            group = anagram_group_map.get(hashable_key, [])
            group.append(word)
            anagram_group_map[hashable_key] = group
        
        return list(anagram_group_map.values())
