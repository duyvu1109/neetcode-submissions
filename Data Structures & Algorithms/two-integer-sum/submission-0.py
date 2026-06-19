class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i, n in enumerate(nums):
            if n not in maps:
                maps[target -n] = i
            else:
                return [maps[n], i]