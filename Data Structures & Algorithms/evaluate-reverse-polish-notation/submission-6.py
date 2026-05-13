def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return int(x / y)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_processor_map = {
            "*": multiply,
            "+": add,
            "-": subtract,
            "/": divide
        }

        eval_stack = []
        for val in tokens:
            if val in operator_processor_map:
                val2 = eval_stack.pop()
                val1 = eval_stack.pop()
                
                res = operator_processor_map[val](val1, val2)
                eval_stack.append(res)
            else:
                eval_stack.append(int(val))
        
        return eval_stack.pop()

