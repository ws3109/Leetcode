class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        heap = []
        for n, c in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (c, n))
            elif heap[0][0] < c:
                heapq.heappop(heap)
                heapq.heappush(heap, (c, n))
        return [n for c, n in heap]
