# Напишите функцию, которая проверяет: является ли слово палиндромом

def palindrome(word):
    if word == word[::-1]:
        return 'Слово является палиндромом.'
    else:
        return 'Слово не является палиндромом.'


user_in = input('Введите слово: ')
print(palindrome(user_in))
