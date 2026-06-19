class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_array = []
        for s in strs:
            if s == "":
                encoded_array.append("empty")
            else:
                temp = []
                for i in range(len(s)):
                    temp.append(str(ord(s[i])))
                encoded_array.append("_".join(temp))
        encoded_string = "-".join(encoded_array)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        if s == '':
            return []
        for i in s.split('-'):
            st = ""
            for j in i.split('_'):
                if j == "empty":
                    st = ""
                    continue
                else:
                    st += chr(int(j))
            result.append(st)
        return result