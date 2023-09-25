class bank:
    def __init__(self):
        self.customer = {}
    def create_account(self,acc_num,bal=0):
        if acc_num in self.customer:
            print("Account number exists")
        else:
            self.customer[acc_num]=bal
            print("Account created")
    def deposit(self,acc_num,amt):
        if acc_num in self.customer:
            self.customer[acc_num]+=amt
            print("Deposit successful")
        else:
            print("Account number does not exist")
    def withdraw(self,acc_num,amt):
        if acc_num in self.customer:
            if self.customer[acc_num]>=amt:
                self.customer[acc_num]-=amt
                print("Withdrawal successful")
            else:
                print("Please check your balance")
        else:
            print("Account number does not exist")
    def check_balance(self,acc_num):
        if acc_num in self.customer:
            bal = self.customer[acc_num]
            print("Account balance: ",bal)
        else:
            print("Account number does not exist")

def bank_operations(bk,ch):
    if ch == 1:
        acc_num = input("Enter account number ")
        bk.create_account(acc_num)
    elif ch == 2:
        acc_num = input("Enter account number ")
        wamt = float(input("Enter withdrawal amount "))
        bk.withdraw(acc_num,wamt)
    elif ch == 3:
        acc_num = input("Enter account number ")
        damt = float(input("Enter the amount to deposit "))
        bk.deposit(acc_num,damt)
    elif ch == 4:
        acc_num = input("Enter account number ")
        bk.check_balance(acc_num)
    else:
        print("Wrong choice")

bk = bank()
while(1):
    print("1.Create new account\n2.Withdraw amount\n3.Deposit amount\n",end='')
    print("4.Check balance\n5.Exit\nEnter choice ")
    ch = int(input())
    if (ch != 1) and (ch!=2) and (ch!=3) and (ch!=4):
        break
    bank_operations(bk,ch)