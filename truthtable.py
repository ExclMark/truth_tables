print("-----TRUTH TABLE SOLVER-----")
print("Made by ExclMark")
print()
print("Help: ")
print("! - NOT")
print("& - AND")
print("| - OR")
print("^ - XOR")
print()
print("Maximum 3 inputs! A, B, and C!")
print()
print("Input example: A|B")

from os import system
system("") # This is just for Windows' CMD to display colors properly.

def prepare_expression(expression: str) -> str:
    expression = expression.replace(" ", "")
    expression = expression.replace("AND", "&")
    expression = expression.replace("OR", "|")
    expression = expression.replace("NOT", "~")
    expression = expression.replace("XOR", "^")
    
    return expression

def validate_expression(expression: str) -> bool:
    operators = ["~", "&", "|", "^", "(", ")"]

    expression = [l for l in expression]

    for exp in expression:
        if exp in ["A", "B", "C"] or exp in operators:
            continue
        else:
            return False
    
    try:
        expression = [l + " " for l in expression]
        expression = "".join(expression)
        if len(expression) <= 2:
            return False
        A = 0
        B = 0
        C = 0
        int(eval(expression.replace("~", "not")))
    except SyntaxError:
        return False

    return True

def calculate_table(expression: str) -> list | list:
    inputs = []
    val = []
    
    expr_set = set(expression)
    for inp in expr_set:
        if inp in ["A"]:
            inputs.append("A")
        if inp in ["B"]:
            inputs.append("B")
        if inp in ["C"]:
            inputs.append("C")

    if len(inputs) == 1:
        val = [1, 0]
    elif len(inputs) == 2:
        val = [[1, 1], [1, 0], [0, 1], [0, 0]]
    elif len(inputs) == 3:
        val = [[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
    
    return val, inputs

def print_table(expression: str, val: list, inputs: list) -> None:
    expression = [l + " " for l in expression]
    expression = "".join(expression)
    
    inputs.sort()

    color_inputs = "\033[0m | \033[94m".join(inputs)
    color_inputs = "\033[94m" + color_inputs + "\033[0m | "

    inputs = " | ".join(inputs)
    inputs = inputs + " | "

    if inputs != expression:
        print(color_inputs, end="")
    print("\033[94m" + expression + "\033[0m")

    i = 0
    A = 0
    B = 0
    C = 0

    space = " " * (int(len(expression) / 2) - 1)

    if len(val) == 2:
        for x in val:
            if inputs[0] == "A":
                A = x
            elif inputs[0] == "B":
                B = x
            elif inputs[0] == "C":
                C = x
            ex = int(eval(expression.replace("~", "not")))
            print(f"{x} | {space}{ex}")
    elif len(val) == 4:
        for x in val:
            i = 0
            for y in x:
                if i == 0:
                    if inputs[0] == "A":
                        A = y
                    elif inputs[0] == "B":
                        B = y
                    elif inputs[0] == "C":
                        C = y
                else: 
                    if inputs[4] == "A":
                        A = y
                    elif inputs[4] == "B":
                        B = y
                    elif inputs[4] == "C":
                        C = y
                i += 1
                print(f"{y} |", end=" ")
            ex = int(eval(expression.replace("~", "not")))
            print(f"{space}{ex}")
    elif len(val) == 8:
        for x in val:
            i = 0
            for y in x:
                if i == 0:
                    if inputs[0] == "A":
                        A = y
                    elif inputs[0] == "B":
                        B = y
                    elif inputs[0] == "C":
                        C = y
                elif i == 1:
                    if inputs[4] == "A":
                        A = y
                    elif inputs[4] == "B":
                        B = y
                    elif inputs[4] == "C":
                        C = y
                else: 
                    if inputs[8] == "A":
                        A = y
                    elif inputs[8] == "B":
                        B = y
                    elif inputs[8] == "C":
                        C = y
                i += 1
                print(f"{y} |", end=" ")
            ex = int(eval(expression.replace("~", "not")))
            print(f"{space}{ex}")

if __name__ == "__main__":
    while True:
        expr = input("Enter expression: ").upper()
        expr = prepare_expression(expr)

        if not validate_expression(expr):
            print("Invalid expression!")
        else:
            val, inputs = calculate_table(expr)
            print_table(expr, val, inputs)
