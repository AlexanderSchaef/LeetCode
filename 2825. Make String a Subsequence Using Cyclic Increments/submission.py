class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        str1_alt = ""
        # Increment the character and store the alternate value
        # Each position can either stay the same or shift up 1 character cyclically a-z
        # lowercase english letters, perform UTF-8 + 1 with cycle on z
        for char in str1:
            utf = ord(char)
            if utf == 122:
                utf = 97
            else:
                utf += 1
            str1_alt += chr(utf)

        # See if a subsequence is possible using the set of allowable characters
        subsequence_pointer = 0
        subsequence_builder = ""
        for i, char in enumerate(str1):
            if str2[subsequence_pointer] == str1[i]:
                
                # The character in str2 is possible to generate in str1
                subsequence_builder += char # add that char to our checker

                if subsequence_builder == str2:
                    # The substring has been found
                    return True
                else:
                    # there are more chars in str2 to find in str1
                    subsequence_pointer += 1
            
            elif str2[subsequence_pointer] == str1_alt[i]:
                
                # char in str2 is found with the increment
                subsequence_builder += str1_alt[i]
                
                if subsequence_builder == str2:
                    return True
                else:
                    # More chars to find in str2
                    subsequence_pointer += 1
                
        # Substring was not found
        return False


            
