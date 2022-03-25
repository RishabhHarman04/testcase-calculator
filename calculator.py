def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y
if __name__ == "__main__":
    num1 = int(input("enter first no."))
    num2 =  int(input("enter second no."))
    print(add(num1,num2))
    print(sub(num1, num2))
    print(mult(num1, num2))
    print(div(num1, num2))