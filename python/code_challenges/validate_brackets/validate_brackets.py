

def validate_brackets(str):
    # store the opening brackets as a  key and closing as a value
    brackets = {"(": ")", "{": "}", "[": "]"}
    # list to hold the stack
    stack = []
    if len(str) == 0:
        return True
    for char in str:
        # check and append if it is an opening bracket
        if char in brackets.keys():
            stack.append(char)
            # print(stack)
        else:
            if len(stack) == 0:
                return False

            closing = stack.pop()

            if char != brackets[closing]:
                return False
        # if the stack is empty at the end return true
        if len(stack) == 0:
            return True
    # if there are some value left after all the string then return false
    return False


# Test code

# str0 = "[]"  # True
# print(str0, "-", validate_brackets(str0))

# str1 = "{}" # True
# print(str1,"-", validate_brackets(str1))

# str2 = "()[[abc]]" # True
# print(str2,"-", validate_brackets(str2))

# str3 = "[{})]" # False
# print(str3,"-",validate_brackets(str3))
