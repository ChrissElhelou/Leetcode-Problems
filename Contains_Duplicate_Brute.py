# O(n^2) time complexity since we regard two nestled loops of length n
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         """Returns true if list contains duplicate elements, false otherwise"""
        # First take each element in the list
        for i in range(len(nums)):
            #Then compare it with all the other elements in the list
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    return True
        return False