import Account_module

name = input('Enter your name: ')
initial_deposit = float(input('Enter your Initial Deposit: '))
my_acc = Account_module.BankAccount(name, initial_deposit)
print(my_acc)

action = input('\nEnter 0 to Quit, 1 for Withdraw, 2 for Deposit, 3 to Print a Ledger')
while True:
    if action == '0':
        print('Thank you and Goodbye.')
        break
    elif action == '1':
        withdraw = float(input('Enter the amount to Withdraw: $'))
        my_acc.withdraw(withdraw)

    elif action == '2':
        deposit = float(input('Enter the amount for Deposit: $'))
        my_acc.deposit(deposit)

    elif action == '3':
        my_acc.see_ledger()
    action = input('\nEnter 0 to Quit, 1 for Withdraw, 2 for Deposit, 3 to Print a Ledger')

