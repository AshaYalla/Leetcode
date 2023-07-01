class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}
        
        def A(curm,curn,ind):
            
            if (curm,curn,ind) in dp:
                return dp[(curm,curn,ind)]
            #if it is less than the capacity return -1
            if curm<0 or curn<0:
                return -1
            #if the ind reached end of the array
            if ind==len(strs):
                return 0
            
            ans1,ans2=0,0
            
            #skip 
            ans1=A(curm,curn,ind+1)
            
            #include 
            ans2=1+A(curm-(strs[ind].count('0')),curn-(strs[ind].count('1')),ind+1)
            
            #store the value
            dp[(curm,curn,ind)]=max(ans1,ans2)
			
            #return the value
            return max(ans1,ans2)
        
        return A(m,n,0)
        