class Solution(object):
    def decodeString(self, s):
        num_stack = []
        string_stack = []
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                num_stack.append(current_num)
                string_stack.append(current_string)
                current_num = 0
                current_string = ""
            elif char == ']':
                num = num_stack.pop()
                previous_string = string_stack.pop()
                current_string = previous_string + current_string * num
            else:
                current_string += char

        return current_string