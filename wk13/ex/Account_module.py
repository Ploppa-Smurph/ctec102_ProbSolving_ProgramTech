class BankAccount:
    def __init__(self, name, initial_amount):
        self.__name = name
        self.__amount = initial_amount
        self.__ledger = [('Initial: $', initial_amount)]

# set getters and setters for the name
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name

    def see_ledger(self):
        for item in self.__ledger:
            print('Transaction: ', item[0], '\tBalance: $', item[1])

    def withdraw(self, value):
        if self.__amount >= value:
            self.__amount -= value
            print('Withdraw Amount: $' + str(value))
            print('New Total: $' + str(self.__amount))
            self.__ledger.append(('Withdraw', self.__amount))
        else:
            print('Insufficient Funds in the account. Current Amount: $' + str(self.__amount))

    def deposit(self, value):
        self.__amount += value
        print('You have deposited: $' + str(value))
        print('New Total: $' + str(self.__amount))
        self.__ledger.append(('Deposit', self.__amount))

    def __str__(self):
        return 'This is ' + self.__name + '\'s account. It has a balance of: $' + str(self.__amount)


'''my_acc = BankAccount('Jeff', 750)
print(my_acc)
my_acc.withdraw(4500)
my_acc.withdraw(666)
my_acc.deposit(825)
my_acc.see_ledger()'''
