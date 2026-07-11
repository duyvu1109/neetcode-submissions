class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[r] + numbers[l] < target:
                l += 1
            if numbers[r] + numbers[l] > target:
                r -= 1
            print(l, r)
        
        return [l+1, r+1]