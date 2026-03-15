class Phone():
    def __init__(self,brand,battery):
        self.brand=brand
        self.__battery=battery
    def get_battery(self):
        return self.__battery
    def charge(self,amount):
        self.__battery+=amount
        if self.__battery>100:
            self.__battery=100
            print('Fully charged')
    def use(self,amount):
        if amount>self.__battery:
            print('low battery')
        else:
            self.__battery-=amount
    def info(self):
        print(f'{self.brand}-battery:{self.__battery}')
    

phone = Phone("Apple", 50)

print(phone.get_battery())  # 50
phone.charge(30)
print(phone.get_battery())  # 80
phone.charge(50)            # Fully charged
print(phone.get_battery())  # 100
phone.use(30)
print(phone.get_battery())  # 70
phone.use(999)              # Low battery
print(phone.get_battery())  # 70
phone.info()                # Apple — battery: 70%