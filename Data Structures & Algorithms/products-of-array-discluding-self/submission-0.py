class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i, n in enumerate(nums):
            # print(nums[0:i], nums[i+1:len(nums)])
            result[i] = math.prod(nums[0:i]) * math.prod(nums[i+1:len(nums)])
        return result
