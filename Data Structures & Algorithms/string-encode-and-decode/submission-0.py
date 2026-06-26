class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string))
            encoded_string += "%%%%"
            encoded_string += string
            encoded_string += "%%%%"
        return encoded_string


    def decode(self, s: str) -> List[str]:
            decoded_strs = []
            new_string = ""
            while len(s) > 0:
                # Find the length of the string
                prefix = s.find("%%%%")
                # Length of string will be whatever is before prefix
                len_str = int(s[:prefix])
                # Start of decoded message is prefix + %%%%
                start = prefix + 4
                # End length of string
                end = start + len_str
                new_string = s[start:end]
                # Add to list
                decoded_strs.append(new_string)
                new_string = "" 
                # Delete Everything before new prefix
                s=s[end + 4:]
            return decoded_strs

                    


