class Task():
    def __init__(self,title):
        self.__title=title
        self.__done=False
    
    def get_title(self):
        return self.__title
    def is_done(self):
        return self.__done
    

    def complete(self):
        self.__done=True 
        
    def info(self):
        if self.__done==True:
            print(f'[x] {self.__title}')
        else:
            print(f'[] {self.__title}')
class TodoManager():
    def __init__(self):
        self.__tasks=[]
    def add_task(self,title):
        task=Task(title)
        self.__tasks.append(task)
        print(f'Add {title}')
    def show_all(self):
        if len(self.__tasks)==0:
            print('there are no tasks')
            return
        for task in self.__tasks:
            task.info()
    def complete_task(self,number):
        if number <1 or number > len(self.__tasks):
            print('нет такой задачи ')
            return
        self.__tasks[number -1].complete()
        print (f'выполнено')
    def delete_task(self,number ):
        if number <1 or number >len(self.__tasks):
            print('нечего удалять ')
            return
        self.__tasks.pop(number-1)
    def show_pending(self):
        for task in self.__tasks:
            if task.is_done()==False:
                task.info()
manager = TodoManager()

while True:
    print("\n1. Добавить задачу")
    print("2. Показать все")
    print("3. Выполнить задачу")
    print("4. Удалить задачу")
    print("5. Невыполненные")
    print("0. Выход")

    try:
        choice = int(input("\nВыбор: "))
    except ValueError:
        print("Введите число")
        continue

    if choice == 1:
        title = input("Название: ")
        manager.add_task(title)
    elif choice == 2:
        manager.show_all()
    elif choice == 3:
        number = int(input("Номер задачи: "))
        manager.complete_task(number)
    elif choice == 4:
        number = int(input("Номер задачи: "))
        manager.delete_task(number)
    elif choice == 5:
        manager.show_pending()
    elif choice == 0:
        print("Пока!")
        break
