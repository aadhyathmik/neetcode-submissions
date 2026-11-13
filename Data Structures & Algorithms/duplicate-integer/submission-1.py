class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = {}
        for num in nums:
            if num not in dupes:
                dupes[num] = 1
            
            elif num in dupes:
                return True

        return False
        

        
