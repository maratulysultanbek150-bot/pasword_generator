from secrets import choice

def gen_password(lenght, chars):
    password = ''
    for i in range(lenght):
        password += choice(chars)
    return password
DIGITS = '0123456789' 
LOWER_ALPHABET = 'qwertyuiopasdfghjklzxcvbnm'
UPPER_ALPHABET = 'QWERTYUIOPASDFGHJKLZXCVBNM'
PUNCTUATION = '!#$%&*+-=?@^_'
char = ''    # Все символы указанные пользователем

print('Количество паролей для генерации:')   
counter = int(input())

print('Длинна одного пароля:')
password_len = int(input())

print('Включать ли цифры? (Да/Нет)')
if input().strip().lower() == 'да':
    char += DIGITS

print('Включать заглавные буквы? (Да/Нет)')
if input().strip().lower() == 'да':
    char += UPPER_ALPHABET

print('Включать ли строчные буквы? (Да/Нет)')
if input().strip().lower() == 'да':
    char += LOWER_ALPHABET

print('Включать ли символы? (Да/Нет)')
if input().strip().lower() == 'да':
    char += PUNCTUATION

for i in range(counter):
    print(gen_password(password_len, char))