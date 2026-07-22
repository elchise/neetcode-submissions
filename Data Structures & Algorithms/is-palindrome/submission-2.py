class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        beg=0
        end=len(s)-1
        while(beg < len(s)/2):
            if(s[beg] != s[end]):
                return False
            beg+=1
            end-=1
        return True
        