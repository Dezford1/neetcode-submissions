class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        while the length of ans is not the length of 2*n array, continue
        append the index of nums to ans increment the index by 1, repeat
        '''
        ans = []
        while len(ans) != len(2*nums):
            for i in nums:
                ans.append(i)
        return ans
                

        