class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        vowels="aeiouAEIOU"
        digit=0
        vowel=0
        consonant=0
        all_characters=0
        for c in word:
            if c.isdigit():
                digit+=1
            if c.isalpha():
                if c in vowels:
                    vowel+=1
                else:
                    consonant+=1
            if not c.isalnum():
                return False
        all_characters=vowel+consonant+digit
        print(vowel)
        print(consonant)
        print(digit)
        print(all_characters)
        if vowel>=1 and consonant>=1 and all_characters >=3:
            return True
        return False