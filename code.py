#question1_A
L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]

A= dict(zip(L1, L2))

print(A)

#question2_B
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of {num} is {factorial(num)}")

#question1_C
L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

for item in L:
    if item.startswith('B'):
        print(item)

#question1_D
d = {i: i+1 for i in range(11)}
print(d)

#question2
# Read the binary number from the user
binary_num = input("Enter a binary number: ")

# Convert the binary number to decimal
decimal_num = 0
for i in range(len(binary_num)):
    digit = int(binary_num[i])
    decimal_num += digit * 2**(len(binary_num)-1-i)

# Display the equivalent decimal number
print(f"The equivalent decimal number of {binary_num} is: {decimal_num}")

#question3

import json
filename="C:\\Users\\HP\\Desktop\\qu.json"
with open(filename,"r") as file:
    q=json.load(file)
unam=input("Enter your name:")
grad=0
for i in range(0,20):
    print(q[i]["question"])
    ans=input("Enter your answer:")
    if ans == q[i]["answer"]:
        grad +=1
res={f"username {unam}  result {grad/20}"}
fileresult="C:\\Users\\HP\\Desktop\\ans.json"
with open(fileresult,"w") as f:
    d=json.dump(res,f)

#question4
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")
    
    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
    
    def print(self):
        print(f"Current balance: {self.balance}")
        print(f"Interest rate: {self.interest_rate}")

# Create an instance of BankAccount
bank_account = BankAccount("123456789", "John Doe")
bank_account.deposit(1000)
print(f"Current balance: {bank_account.get_balance()}")
bank_account.withdraw(500)
print(f"Current balance: {bank_account.get_balance()}")

# Create an instance of SavingsAccount
savings_account = SavingsAccount("987654321", "Jane Smith", 0.05)
savings_account.deposit(1000)
savings_account.apply_interest()
savings_account.print()