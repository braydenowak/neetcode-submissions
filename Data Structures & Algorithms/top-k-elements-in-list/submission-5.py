class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter -> you get the counts of each number
        # coutner class should have a call to return most frequent
        # any order -> need to conver to a list
        cntr = Counter(nums)
        res = cntr.most_common(k)

        return [num for num,count in res]
        