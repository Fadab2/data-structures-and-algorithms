

def validate_brackets(str):

        brackets = {"(": ")","{": "}","[": "]"}

        stack = []

        for char in str:
            if char in brackets.keys():
                stack.append(char)
                print(stack)
            else:
                if len(stack)== 0:
                    return False

                closing = stack.pop()
                print(f'closing {closing}')
                # validate the closing bracket
                if char != brackets[closing]:
                    return False

            return len(stack) == 0


str = "{}" # True
print(str,"-", validate_brackets(str))

str = "()[[Extra Characters]]" # True
print(str,"-", validate_brackets(str))

str = "[({}]" # False
print(str,"-",validate_brackets(str))

