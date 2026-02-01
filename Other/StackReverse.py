stack1 = [1, 2, 3, 4]

def reverse_stack(stack: list[int]):
    res = []
    reverse_stack_unit(stack, res)
    stack[:] = res
    return stack

def reverse_stack_unit(stack, result):
    if len(stack) == 0:
        return
    else:
        cur = stack.pop()
        result.append(cur)
        reverse_stack_unit(stack, result)

reverse_stack(stack1)
print(stack1)
