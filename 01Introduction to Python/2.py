from collections import OrderedDict as od
import re

# od.fromkeys([i for i in key_word.lower()])

def encoder(key_word, users_str): # функция "кодировшик"
    '''Encoder function. There are two required parameters.
    "key_word" is оne-word string of letters.
    "users_str" is string of one or more words separated by spaces.'''
    alfa = 'abcdefghijklmnopqrstuvwxyz' # алфавит
    key_word_lst = [i for i in key_word.lower()] # словарь из отдельных букв ключевого слова
    code = ''
    for i in alfa: # цикл отсеивания букв из алфавита
        if i not in key_word_lst:
            code += i
    # убираем дубликаты с помощью OrderedDict и соединяем строки
    encryption_key = ''.join(list(od.fromkeys(key_word_lst))) + code # ключ шифрования
    result = ''
    for i in users_str: # цикл шифрования
        if i != ' ':
            result += encryption_key[alfa.find(i)] # взятие букве по позиции из алфавита
        else:
            result += ' '
    return result

class LstChecker():
    def super_isalpha(self, s):
        for i in s.split(' '):
            if i.isalpha() == True:
                continue
            else:
                return False
        return True

if __name__ == '__main__':
    # запуск проверок на отсутсвие цифр и лишних символов
    # предполагается что слова будут на Английском языке
    key_word = input('Введте слово: ')
    # Попытка применить проверку на язык с помощью re, нужна отдельная функция
    pattern = re.compile(r'[a-zA-z]+', re.ASCII)
    check_lang = re.match(pattern, key_word)

    while key_word.isalpha() != True or check_lang == None:
        key_word = input('Неверный ввод, попробуйте еще раз: ')
        check_lang = re.match(pattern, key_word)
    users_str = input('Фразу, которую нужно зашифровать: ')
    while LstChecker().super_isalpha(users_str) != True:
        users_str = input('Неверный ввод, попробуйте еще раз: ')
    # Вывод результата функции "шифратора (encoder)" с параметрами:
    # 1) ключевое слово 2) Строка которую нужно зашифровать
    print(encoder(key_word, users_str).upper()) # upper опционально
