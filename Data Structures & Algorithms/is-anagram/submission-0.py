class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            maps = {}
            mapt = {}
            for i in range(len(s)):
                if s[i] not in maps:
                    maps[s[i]] = 1
                else:
                    maps[s[i]] += 1
                if t[i] not in mapt:
                    mapt[t[i]] = 1
                else:
                    mapt[t[i]] += 1
            for j in maps:
                if maps.get(j) != mapt.get(j):
                    return False
            return True