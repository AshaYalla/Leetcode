#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        dictt = {}
        def subset(i,total):
            if (i,total) in dictt:
                return dictt[(i,total)]
            if total == 0:
                return 1
        
            if i == N:
                return 0
            c1 = 0
            if arr[i] <= total:
                c1 = subset(i+1, total-arr[i])
            c2 = subset(i+1, total)
            dictt[(i,total)] = c1+c2
            return c1+c2
        if subset(0,sum) == 0:
            return False
        else:
            return True
        
            
                
                
                
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends