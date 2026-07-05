class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for s in strs:
            encodedStr += s + "$#"
        
        print(encodedStr)
        return encodedStr

    def decode(self, s: str) -> List[str]:
        
        return s.split("$#")[:-1]
