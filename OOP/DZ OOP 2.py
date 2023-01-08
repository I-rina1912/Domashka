""" Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letter - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letter_num(), который вернет кол-во букв в алфавите"""

from string import ascii_uppercase


"""Класс EngAlphabet
1. Создайте класс EngAlphabet путем наследования от класса Alphabet
2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
В качестве параметров ему будут передаваться обозначение языка(например,'En') и строка, состоящая из всех букв
алфавита (можно воспользоваться свойством ascii_uppercase из модуля string).
3. Добавьте приватное статическое свойство __letters_num, которое будет хранить кол-во букв в алфавите
4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять,
относится ли эта буква к анг.алфавиту
5. Переопределите метод letters_num - пусть в текущем классе он будет возвращать значение свойства __letters_num.
6. Создайте статический метод example(), который будет возвращать пример текста на анг.языке"""


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def __str__(self):
        return str(self.letters)

    def letter_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    def __init__(self, lang, letters):
        super().__init__(lang, letters)
        self.__letters_num = len(letters)

    def is_en_letter(self, letter):
        if letter in self.letters:
            print('True')
        else:
            print('False')

    def letter_num(self):
        return self.__letters_num

    @staticmethod
    def example():
        return 'HELLO WORLD!'


a = Alphabet('ru', ['a', 's', 'd', 'y'])
print(a)
print(a.letter_num())

b = EngAlphabet('En', list(ascii_uppercase))
print(b)
b.is_en_letter('F')
print(b.letter_num())
print(b.example())
