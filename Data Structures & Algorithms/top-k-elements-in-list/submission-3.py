class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        res = cntr.most_common(k)

        return [num for num,count in res]