class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0
        ls=[]
        
        for i in range(len(p),len(s)+1):
            m1=s[l:i]
            m=list(set(m1))
            q=list(set(p))
            c=0
            for j in range(len(q)):
                if len(m)==len(q) and m[j] in q :
                    cnt1=m1.count(m[j])
                    cnt=p.count(m[j])
                    if cnt1==cnt:

                        c+=1
            if c==len(q):
                ls.append(l)
            l+=1
        return ls



        
