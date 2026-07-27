class Solution:

    def encode(self, strs: List[str]) -> str:

        encoding = ""

        for i in strs:
            encoding += str(len(i)) + "#" + i
        return encoding


    def decode(self, s: str) -> List[str]:
        decoding, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) 
            decoding.append(s[j+1 : j + 1 + length])
            i = j + 1 + length

        return decoding
