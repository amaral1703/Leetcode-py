class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        contador = 0
        for i in range(len(nums)):
            if  i < (len(nums)-1) and nums[i] == nums[i+1]:
                continue 
            nums[contador] = nums[i]
            contador += 1
        return contador