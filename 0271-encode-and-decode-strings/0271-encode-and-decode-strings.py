class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encode = ""
        for i in strs:
            encode +=str(len(i)) + '/:' + i
        return encode
            
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        
        """
        ans = []
        i = 0
        while i < len(s):
            ind = s.find('/:',i)
            leng = int(s[i:ind])
            ans.append(s[ind+2:ind+2+leng])
            i = ind+2+leng
        return ans
            
        
        
        
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))