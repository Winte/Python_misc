class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [key for key, value in collections.Counter(nums).most_common(k)]