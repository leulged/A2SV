class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls=0
        for i in range(len(s)):
            st=''
            for j in range(i,len(s)):
                if s[j] not in st:
                    st+=s[j]
                else:
                    break
            ls=max(len(st),ls)
        return ls

        
