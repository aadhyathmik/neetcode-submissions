from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_k = heapq.nlargest(k, count.keys(), count.get)
        return top_k
