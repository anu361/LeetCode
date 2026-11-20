class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}
        l=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        new = sorted(d,key=d.get, reverse=True)  
        return new[:k]      

        
        