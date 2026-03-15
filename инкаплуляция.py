class Student():
    def __init__(self,name,grade):
        self.__name=name # __ = скрытый атрибут, напрямую не менять
        self.__grade=grade
    def get_name(self):# геттер — читаем скрытый атрибут
        return self.__name
    def get_age(self):
        return self.__grade
    def set_grade(self,grade):# сеттер — меняем с проверкой
        if self.__grade <0 or self.__grade>10:
            print('неверная оценка')
        else:
            self.__grade= grade # меняем только если проверка прошла
    def info(self):
        print(f'{self.__name}-grade:{self.__grade}')


student=Student('amir',5)
print(student.info())