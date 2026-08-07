class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxCount = 0

        for num in nums:
            if num - 1 not in nums_set:
                start = num
                counter = 1

                while num + counter in nums_set:
                    counter += 1
            
                maxCount = max(counter, maxCount)

        return maxCount

            



            
