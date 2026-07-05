class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        cleaned_text = "".join(char for char in s if char.isalnum()).lower()
        l, r = 0, len(cleaned_text) - 1
        while l < r:
            # print(cleaned_text[l], cleaned_text[r])
            if cleaned_text[l] != cleaned_text[r]:
                return False
            l += 1
            r -= 1
        return True