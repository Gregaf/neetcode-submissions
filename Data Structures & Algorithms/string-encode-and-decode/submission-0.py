class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_data = ""
        for chunk in strs:
            encoded_data += "{}#{}".format(len(chunk), chunk)
        
        return encoded_data

    def decode(self, s: str) -> List[str]:
        l = 0
        r = l
        
        len_encoding = len(s)

        decoded_chunks = []
        while l < len_encoding:
            while r < len_encoding and s[r] is not "#":
                r += 1
            
            len_text = int(s[l:r])
            i = r + len_text + 1
            decoded_chunk = s[r + 1:i]
            decoded_chunks.append(decoded_chunk)
            l = i
            r = i
        
        return decoded_chunks
            
            
