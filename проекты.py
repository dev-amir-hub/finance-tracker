class FinanceTraker:#это мой 1
    def __init__(self,owner):
        self.owner = owner
        self.balance=[]


    def dobavit(self,amount,opis):
        operation = {
            "type":"income",
            'amount':amount,
            'opis':opis
        }
        self.balance.append(operation)
        print(f'добавлено +{amount} рублей')



    def ubavit(self,amount,opis):
        operation = {
            "type":"expence",
            'amount':amount,
            'opis':opis
        }
        self.balance.append(operation)
        print(f'потрачено -{amount} рублей')


    def show_balance(self):
        income=0
        expence=0
        for money in self.balance:
            if money['type']=='income':
                income+=money['amount']
            else:
                expence+=money['amount']
        print(f'\n Трекер:{self.owner}')
        print(f'заработано {income} руб')
        print(f'потрачено {expence} руб')
        print(f'баланс:{income-expence} руб')


    def history(self):
        if len(self.balance)==0:
            print('ничего не добавляли')
        for money in self.balance:
            if money['type']=='income':
                print(f'+{money['opis']}--{money["amount"]}')
            else:
                print(f'-{money['opis']}--{money["amount"]}')

tracker=FinanceTraker('Амип')
print(f'Финаносвоый трекер {tracker.owner}')
while True:
    print("\n1  добавить доход")
    print("2  добавить расход")
    print("3  показать баланс")
    print("4  показать историю")
    print("5  выход")

    try:
        choise = int(input())
    except ValueError:
        print("введите число от 1 до 5")
        continue

    if choise == 1:
        amount = float(input("сколько заработали: "))
        opis = input("описание: ")
        tracker.dobavit(amount, opis)  # вызываем метод объекта
    elif choise == 2:
        amount = float(input("сколько потратили: "))
        opis = input("описание: ")
        tracker.ubavit(amount, opis)
    elif choise == 3:
        tracker.show_balance()
    elif choise == 4:
        tracker.history()
    elif choise == 5:
        print("Досвидания!")
        break