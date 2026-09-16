class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #hash map for the counts of each number
        freq = [[] for i in range(len(nums) + 1)]
        #freq is a 2D array with the rows being 0 - the total number of numbers in num + 1
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        #we go through the array nums and use the num as a key for the hash, each time we find a number we key it and add 1 to is value, if there is no value 0 is used as fallback
        for num, cnt in count.items():
            freq[cnt].append(num)
        #now we go through hashes items and we map our arrays indexs for the count and add in the number that has that count
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        #creates our return array