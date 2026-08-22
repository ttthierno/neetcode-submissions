class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in ans:
                return [ans[difference], i]
            ans[n] = i