# Faulty Keyboard

class Solution(object):
    def finalString(self, s):
        result = ''
        is_reversed = False
        
        for char in s:
            if char == 'i':
                is_reversed = not is_reversed
            else:
                if is_reversed:
                    result = char + result
                else:
                    result += char
        
        if is_reversed:
            result = result[::-1]
        
        return result
    
solution = Solution()
print(solution.finalString("string"))
