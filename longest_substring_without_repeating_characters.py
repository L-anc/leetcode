class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        longest = 0
        i = 0
        while i < len(s):
            print(f"longest: {longest}")
            print(f"i: {i}")
            if seen_chars.get(s[i]) is not None:
                if len(seen_chars.keys()) > longest:
                    longest = len(seen_chars.keys())
                    print(f"new longest: {longest}")
                    print(f"seen_chars: {seen_chars}")
                i = seen_chars[s[i]] + 1
                seen_chars = {}
            else:
                seen_chars[s[i]] = i
                print(f"seen_chars: {seen_chars}")
                i += 1

        if len(seen_chars.keys()) > longest:
            longest = len(seen_chars.keys())
        return longest
    
    # Same O(n) time complexity but faster on most inputs
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Expected output: 3
print(sol.lengthOfLongestSubstring("bbbbb"))     # Expected output: 1
print(sol.lengthOfLongestSubstring("pwwkew"))    # Expected output: 3
print(sol.lengthOfLongestSubstring("pdwowkes"))    # Expected output: 5