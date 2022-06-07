class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        for char in ransom_note:
            if char in magazine:
                idx = magazine.index(char)
                magazine = magazine[0:idx] + magazine[idx + 1 :]
            else:
                return False
        return True
