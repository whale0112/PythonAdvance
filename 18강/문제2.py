def calc(numA, numB, exp):
    if exp == '+':
        return numA + numB
    elif exp == '-':
        return numA - numB
    elif exp == '*':
        return numA * numB
    
def get_operator_index(exp):
    for index, value in enumerate(exp):
        if value == '+' or value == '-' or value == '*':
            return index
        
def get_numbers(exp, idx):
    numA = int(exp[:idx])
    numB = int(exp[idx + 1:])
    return numA, numB

def solution(expression):
    exp_index = get_operator_index(expression)
    first_num, second_num = get_numbers(expression, exp_index)
    result = calc(first_num, second_num, expression[exp_index])
    return result

expression = "123+12"
ret = solution(expression)
print("Solution: return value of the function is", ret, ".")

expression = "12345-4321"
ret = solution(expression)
print("Solution: return value of the function is", ret, ".")

expression = "123000*120"
ret = solution(expression)
print("Solution: return value of the function is", ret, ".")