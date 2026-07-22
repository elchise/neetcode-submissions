class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l = len(s)-1
        for i in range(0, (l+1)//2):
            if(s[i] != s[l-i]):
                return False
        return True