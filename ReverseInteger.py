class Solution:
    def reverse(self, x: int) -> int:

        negative = False

        if(x < 0):
            negative = True
            x = 0 - x
            
        beforeRevStr = str(x)
        afterRevStr = int(beforeRevStr[::-1])
        
        if(negative):
            afterRevStr = 0 - afterRevStr

        if((afterRevStr < pow(-2,31)) or (afterRevStr  >pow( 2,31) - 1)):
            return 0
        else:
            return afterRevStr
        
