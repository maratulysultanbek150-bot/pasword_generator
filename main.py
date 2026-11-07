from secrets import choice


def gen_password(lenght, chars):
    password = ""
    for i in range(lenght):
        password += choice(chars)
    return password


DIGITS = "0123456789"
LOWER_ALPHABET = "qwertyuiopasdfghjklzxcvbnm"
UPPER_ALPHABET = "QWERTYUIOPASDFGHJKLZXCVBNM"
PUNCTUATION = "!#$%&*+-=?@^_"
char = ""  # Все символы указанные пользователем

print("Количество паролей для генерации:")
try:
    counter = int(input())
except ValueError:
    print("Введите корректое число")
    exit()

print("Длинна одного пароля:")
try:
    password_len = int(input())
except ValueError:
    print("Введите корректное число")
    exit()

print("Включать ли цифры? (Да/Нет)")
if input().strip().lower() == "да":
    char += DIGITS

print("Включать заглавные буквы? (Да/Нет)")
if input().strip().lower() == "да":
    char += UPPER_ALPHABET

print("Включать ли строчные буквы? (Да/Нет)")
if input().strip().lower() == "да":
    char += LOWER_ALPHABET

print("Включать ли символы? (Да/Нет)")
if input().strip().lower() == "да":
    char += PUNCTUATION

if char == "":
    print("В пароле нет никаких символов, попробуй снова")
    exit()


for _ in range(counter):
    print(gen_password(password_len, char))
