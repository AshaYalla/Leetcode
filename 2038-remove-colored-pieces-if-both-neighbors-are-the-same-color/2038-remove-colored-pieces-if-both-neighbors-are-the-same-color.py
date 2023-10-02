class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        n = len(colors)
        if n < 3:
            return False
        
        i = 0
        
        acount = 0
        bcount = 0
        ares = 0
        bres = 0
        
        while i < n:
            if colors[i] == 'A':
                if bcount >2:
                    print(bcount)
                    bres += bcount-2
                bcount = 0
                acount+=1
            else:
                if acount >2:
                    
                    ares += acount-2
                acount = 0
                bcount+=1
                
            
            i+=1
        if acount and acount> 2:
            ares += acount-2
        if bcount and bcount > 3:
            bres += bcount-2
            
            
        return ares > bres
            
            
            
                
        