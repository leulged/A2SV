class Solution:
    def freqAlphabets(self, s: str) -> str:
        ls='abcdefghijklmnopqrstuvwxyz'
        st=[]
        l=0
        while l<len(s):
            if l + 2 < len(s) and s[l + 2] == '#':
                index = int(s[l:l+2]) - 1
                st.append(ls[index])
                l+=3

            else:
                index = int(s[l]) - 1
                st.append(ls[index])
                l += 1
        return ''.join(st)
            
                


            
