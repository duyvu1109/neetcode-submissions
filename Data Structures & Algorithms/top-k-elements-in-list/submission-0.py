class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for n in nums:
            m[n] = 1 + m.get(n, 0)
    
        sorted_data = dict(sorted(m.items(), key=lambda item: item[1], reverse=True))

        return list(sorted_data)[:k]