class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check=set()
        for elem in nums:
            if elem in check:
                return True
            else:
                check.add(elem)
        return False

