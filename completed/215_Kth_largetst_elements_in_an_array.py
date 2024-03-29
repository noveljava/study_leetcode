from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        i = len(nums) - k
        return sorted(nums)[i]


assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
