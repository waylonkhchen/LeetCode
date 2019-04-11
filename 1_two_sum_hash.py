class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index,num in enumerate(nums):
            another_num = target-num
            nums_copy = nums.copy()
            nums_copy.pop(index)
            if another_num in nums_copy:
                if another_num == num:
                    return [index, nums_copy.index(another_num)+1]
                else:
                    return [index, nums.index(another_num)]