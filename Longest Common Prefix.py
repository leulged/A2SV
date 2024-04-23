class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        x=strs[0]
        for i in range(len(x)):
            for j in range(1,len(strs)):
                print(i,strs[j])
                if i>=len(strs[j]) or not (x[i]==strs[j][i]):
                    return s
            s += x[i]
        return s
