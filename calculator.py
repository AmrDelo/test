class calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        num3 = self.num1 + self.num2
        print("Sum: "+str(num3))

    def sub(self):
        num3 = self.num1 - self.num2
        print("Difference: "+str(num3))

    def mul(self):
        num3 = self.num1 * self.num2
        print("Product: "+str(num3))
    
    def div(self):
        num3 = self.num1 / self.num2
        print("Quotient: "+str(num3))

def operation(cal,opt):
    if opt == '1':
        cal.add()
    elif opt == '2':
        cal.sub()
    elif opt == '3':
        cal.mul()
    elif opt == '4':
        cal.div()
    else:
        print("Wrong choice")


print("Enter the 2 numbers\n")
num1 = float(input("Enter first number "))
num2 = float(input("Enter second number "))
print("Enter your choice of operation\n1. Addition\n",end='')
print("2. Subtraction\n3.Multiplication\n4. Division\n")
opt = input()
cal = calculator(num1,num2)
operation(cal,opt)

