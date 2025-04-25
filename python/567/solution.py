class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def f_hash(counter: list[int]):
            return ''.join(f'{chr(i + 97)}{counter[i]}' for i in range(26) if counter[i] > 0)       

        if len(s1) > len(s2):
            return False
        
        counter = [0] * 26
        for ch in s1:
            counter[ord(ch) - 97] += 1
        s1_hash = f_hash(counter)

        window = [0] * 26
        for i in range(len(s2)):
            window[ord(s2[i]) - 97] += 1
            if i >= len(s1):
                window[ord(s2[i - len(s1)]) - 97] -= 1
            print(f"i = {i}, s2[i] = {s2[i]}, window = {window}")
            if f_hash(window) == s1_hash:
                return True
        return False


print(Solution().checkInclusion('a', 'ab'))
print(Solution().checkInclusion('ab', 'eidbaooo'))
print(Solution().checkInclusion('ab', 'eidboaoo'))
            
            
