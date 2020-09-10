class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False

        if (x < 10):
            return True
        
        palindrome = []
        while x >= 10:
            remainder = x % 10
            palindrome.append(remainder)
            x = x // 10
        
        palindrome.append(x)
        print(palindrome)

        x = 0
        i = len(palindrome) - 1
        getPalind = False
        while True:
            if (i <= x):
                return getPalind

            if(palindrome[x] != palindrome[i]):
                return False
            else:
                x += 1
                i -= 1
                getPalind = True
