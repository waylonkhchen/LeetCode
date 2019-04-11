class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,j in enumerate(nums):
            nums_copy = nums.copy()
            nums_copy.pop(i)
            for l,k in enumerate(nums_copy):
                if j+k == target:
                    return [i,l+1]
                