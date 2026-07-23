import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        
        cleaned = re.sub(r'[^a-z0-9]', '', lower_s)

        length = len(cleaned) - 1
        
        for i in range(len(cleaned) // 2):
            if cleaned[i] != cleaned[length]:
                return False
            length -= 1
            
        return True