import random as r


class PasswordCreater():
    '''Class for generating passwords'''
    def __init__(self):
        # Набор символов по умолчанию.
        self.symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklnopqrstuvwxyz1234567890+-/*!&$#?=@<>()'

    def creater(self, q):
        '''Creater of passwords method. There is one required argument "q". q is amount of passwords.'''
        passwords = [] # будующий список с паролями
        # Пока заданное пользователем кол-во паролей не сравняется с 0.
        while q != 0:
            # list comprehension для генерации одного пароля
            password = [r.choice(self.symbols) for i in range(r.randint(6, 20))]
            passwords.append(''.join(password)) # добавление сгенерированного пароля в список passwords
            q -= 1
        return passwords

if __name__ == '__main__':
    amount = input('Введте количество паролей: ')
    # Проверка введенных пользователем данных на наличие букв и символов
    if amount.isdigit() == True:
        # Проверка на пустой запрос или "слишком большое" количсество запрашиваемых одноврем-но паролей
        if int(amount) == 0 or int(amount) > 10000:
            print('<ошибка>')
        else:
            # Вывод в консоль значений списка passwords
            for i in PasswordCreater().creater(int(amount)):
                print(i)
    else:
        print('<ошибка>')
