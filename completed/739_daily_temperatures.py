from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []

        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last

            stack.append(i)

        return answer

print(Solution().dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))
