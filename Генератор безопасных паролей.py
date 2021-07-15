import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать?\n'))
pwd_len = int(input('Какой длины должен быть пароль?\n'))
pwd_digits = input('Включать ли в пароль цифры от 0 до 9? да/нет\n').lower()
pwd_uppercase = input('Включать ли в пароль прописные буквы? да/нет\n').lower()
pwd_lowercase = input('Включать ли в пароль строчные буквы? да/нет\n').lower()
pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? да/нет\n').lower()
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? да/нет\n').lower()
if pwd_digits == 'да':
    chars += digits
if pwd_uppercase == 'да':
    chars += uppercase_letters
if pwd_lowercase == 'да':
    chars += lowercase_letters
if pwd_punctuation == 'да':
    chars += punctuation
if pwd_exceptions == 'да':
    for n in "il1Lo0O":
        chars = chars.replace(n,'')
def generate_pwd(pwd_len,chars):
    password = ''
    for n in range(pwd_len):
        password += random.choice(chars)
    return password2
for _ in range(pwd_quantity):
    generate_pwd(pwd_len,chars)
    print(generate_pwd(pwd_len,chars))


