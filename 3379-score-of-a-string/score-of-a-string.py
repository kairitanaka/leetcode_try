class Solution:
    def scoreOfString(self, s: str) -> int:
        all_ascii = []
        ascii_dict = {}
        score = 0
        for i in range(len(s)-1):
            curr_char = s[i]
            next_char = s[i+1]
            key = curr_char+next_char
            if key in ascii_dict:
                score += ascii_dict[key]
            else:
                total_ascii = abs(ord(curr_char) - ord(next_char))
                ascii_dict[curr_char+next_char] = total_ascii
                score+=total_ascii
        return score
            
            