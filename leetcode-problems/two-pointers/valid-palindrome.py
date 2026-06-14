class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_s = "".join([ch for ch in s if ch.isalnum()])
        
        clean_s = clean_s.lower()
        reverse_clean_s = "".join(reversed(clean_s))

        print(clean_s)
        print(reverse_clean_s)

        return clean_s == reverse_clean_s
