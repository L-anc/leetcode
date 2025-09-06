class Solution:
    # Initial solution uses 2 cursors i and j to find palindromes
    # i increments by 1 every iteration and j decrements by 1 every sub-iteration
    # until matching characters are found then i and j increment and decrement
    # together until they no longer match or they meet (i==j or i+1==j)
    # the program also returns immediately if a palindrome longer than half the string is found
    # as a longer palindrome cannot be found
    def longestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        longest = ""
        while i < len(s):
            while j >= i:
                if s[i] == s[j]:
                    i_saved = i
                    j_saved = j
                    while s[i] == s[j]:
                        if i == j or i+1==j:
                            # found palindrome
                            pal = s[i_saved:j_saved+1]
                            if len(pal) > len(longest):
                                longest = pal
                                if len(longest) > len(s)/2:
                                    # can't find larger
                                    return longest
                            break
                        else:
                            i += 1
                            j -= 1
                    
                    i = i_saved
                    j = j_saved
                j -= 1
            i += 1
            j = len(s) - 1

        return longest
    

    def longestPalindromeImproved(self, s: str) -> str:
        
        
                            
sol = Solution()
print(sol.longestPalindrome("babad")) # Expected output: "bab" or "aba"
print(sol.longestPalindrome("acdebedks")) # Expected output: "debed"
print(sol.longestPalindrome("acdeedks")) # Expected output: "deed"
print(sol.longestPalindrome("cbbd")) # Expected output: "bb"
print(sol.longestPalindrome("bb")) # Expected output: "bb"