from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        counter = 0
        s_set = set()

        while right < len(s):
            if s[right] not in s_set:
                s_set.add(s[right])
                right+=1
                counter = max(counter, right-left)
            else:
                s_set.discard(s[left])
                left += 1
                
        return counter

                
