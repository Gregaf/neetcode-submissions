class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # { anagramGroup1: [], anagramGroup2: [] ...}
        # anagramGroupKey -> sorted anagram
        anagramGroups = defaultdict(list)

        for s in strs:
            countList = [0] * 26

            for c in s:
                countList[ord(c) - ord("a")] += 1
            
            countKey = tuple(countList)
            anagramGroups[countKey].append(s)

        return anagramGroups.values()
        
        # O(n) * O(m log m), Big O, O(n) Memory
        # FIRST PASS - Works but not the best time complexity possible
        # anagramGrouping = {}

        # for anagram in strs:
        #     sortedAnagramKey = "".join(sorted(anagram))
        #     newAnagramGroup = anagramGrouping.get(sortedAnagramKey, [])
            
        #     newAnagramGroup.append(anagram)
        #     anagramGrouping[sortedAnagramKey] = newAnagramGroup
        
        # return anagramGrouping.values()