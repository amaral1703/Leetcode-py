class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapa={}
        for i in nums:
            if i in mapa:
                return True
            mapa[i] = i

        return False
