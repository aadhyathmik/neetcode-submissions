class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            if heights[left] <= heights[right]:
                maxArea = max((right - left) * min(heights[left], heights[right]), maxArea)
                left += 1
            elif heights[right] < heights[left]:
                maxArea = max((right - left) * min(heights[left], heights[right]), maxArea)
                right -= 1


        return maxArea