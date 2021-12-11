# Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

def credit_card_num(number):
    number = str(number)
    for i in number[:-4]:
        number = number.replace(i, '*')

    return number


user_in = int(input('Введите номер карты: '))
print(credit_card_num(user_in))
