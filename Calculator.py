# calculator
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
opertions={"+":add,"-":sub,"*":multiply,"/":divide}
def calculator():
    num1=float(input("Enter the first number:\n"))
    for symbol in opertions:
        print(symbol)
    should_continue=True
    while should_continue:
        operation_symbol=input("Pick an operation:")
        num2=float(input("Enter the next number:\n"))
        calculation_function=opertions[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        recalcualtion=input(f"Type 'y' to contine with {answer}, or type 'n' to exit or start new caluclation:")
        if recalcualtion=='y' or recalcualtion=='Y':
            num1=answer
            should_continue=True
        else:
            should_continue=False
calculator()
