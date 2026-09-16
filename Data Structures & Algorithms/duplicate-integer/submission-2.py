class Solution:
    def heapify(arr, n, i):
        largest = i
        left = 2 * i +1;
        right = 2 * i +2;
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Solution.heapify(arr, n, largest)

    def heapSort(arr):
        n = len(arr)

        for i in range(n//2-1,-1,-1):
            Solution.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            Solution.heapify(arr, i, 0)

        return arr

    def hasDuplicate(self, nums: List[int]) -> bool:
        Solution.heapSort(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False