class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # { anagramGroup1: [], anagramGroup2: [] ...}
        # anagramGroupKey -> sorted anagram
        
        # O(n) * O(m log m), Big O, O(n) Memory
        anagramGrouping = {}

        for anagram in strs:
            sortedAnagramKey = "".join(sorted(anagram))
            newAnagramGroup = anagramGrouping.get(sortedAnagramKey, [])
            
            newAnagramGroup.append(anagram)
            anagramGrouping[sortedAnagramKey] = newAnagramGroup
        
        return anagramGrouping.values()