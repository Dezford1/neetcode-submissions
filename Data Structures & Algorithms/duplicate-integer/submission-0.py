class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_list = []
        for i in nums:
            new_list.append(i)
        set_list = set(new_list)
        if len(set_list) == len(nums):
            return False
        else:
            return True
        