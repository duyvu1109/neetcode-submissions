class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # m = set(nums)
        # seen = {}
        # for n in nums:
        #     if n not in seen:
        #         seen[n] = 1
        #     else:
        #         continue
        #     if n - 1 in m:
        #         if n - 1 in seen:
        #             seen[n] += seen[n-1] - 1
        #         else:
        #             seen[n] += 1
        #     if n + 1 in m:
        #         if n + 1 in seen:
        #             seen[n] += seen[n+1] - 1
        #         else:
        #             seen[n] += 1
        
        # return max(seen.values())
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        m = 1
        count = 1
        for i in range(1, len(nums)):
            # print(nums[i], nums[i-1])
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                count += 1
            else:
                if count > m:
                    m = count
                count = 1
        if m < count:
            return count
        else:
            return m
            