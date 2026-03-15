class FinanceTraker:
    def __init__(self, owner):
        self.owner = owner
        self.balance = []

    def dobavit(self, amount, opis):
        operation = {
            "type": "income",
            "amount": amount,
            "opis": opis
        }
        self.balance.append(operation)
        print(f'добавлено +{amount} рублей')

    def ubavit(self, amount, opis):
        operation = {
            "type": "expense",
            "amount": amount,
            "opis": opis
        }
        self.balance.append(operation)
        print(f'потрачено -{amount} рублей')

    def show_balance(self):
        income = 0
        expense = 0
        for money in self.balance:
            if money['type'] == 'income':
                income += money['amount']
            else:
                expense += money['amount']
        print(f'\nТрекер: {self.owner}')
        print(f'заработано {income} руб')
        print(f'потрачено {expense} руб')
        print(f'баланс: {income - expense} руб')

    def history(self):
        if len(self.balance) == 0:
            print('ничего не добавляли')
            return                              # ← исправлено: добавили return
        for money in self.balance:
            if money['type'] == 'income':
                print(f'+{money["opis"]}--{money["amount"]}')   # ← исправлено: кавычки
            else:
                print(f'-{money["opis"]}--{money["amount"]}')   # ← исправлено: кавычки


tracker = FinanceTraker('Амир')
print(f'Финансовый трекер {tracker.owner}')

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
        tracker.dobavit(amount, opis)
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