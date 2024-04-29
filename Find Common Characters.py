class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words)==1:
            return words
        w1=set(words[0])
        list_t=[]
        for  i in w1:
            n=min(j.count(i) for j in words)
            if n:
                list_t+=[i]*n
        return list_t
