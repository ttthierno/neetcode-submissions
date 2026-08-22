class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        emptySet = set();

        for i in nums:
            if i in emptySet:
                return True;
            else:
                emptySet.add(i)
        return False