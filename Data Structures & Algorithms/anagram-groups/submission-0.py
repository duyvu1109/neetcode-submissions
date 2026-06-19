class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        maps = {}
        
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in maps:
                maps[ss] = [s]
            else:
                maps[ss].append(s)
        for j in maps:
            result.append(maps.get(j))

        return result