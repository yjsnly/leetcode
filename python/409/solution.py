class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = [0] * 52
        for ch in s:
            if ch.islower():
                counter[ord(ch) - 97] += 1
            else:
                counter[ord(ch) - 65 + 26] += 1
        ret = sum(x // 2 * 2 for x in counter)
        return ret if ret == len(s) else ret + 1
    

if __name__ == '__main__':
    print(Solution().longestPalindrome("abccccdd"))
    print(Solution().longestPalindrome("a"))
    print(Solution().longestPalindrome("aaaaaccc"))
        
