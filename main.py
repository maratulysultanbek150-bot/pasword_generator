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

try:
    counter = int(input("Количество паролей для генерации:"))
except ValueError:
    print("Введите корректое число")
    exit()


try:
    password_len = int(input("Длинна одного пароля:"))
except ValueError:
    print("Введите корректное число")
    exit()

if input("Включать ли цифры? (Да/Нет):").strip().lower() == "да":
    char += DIGITS


if input("Включать заглавные буквы? (Да/Нет):").strip().lower() == "да":
    char += UPPER_ALPHABET


if input("Включать ли строчные буквы? (Да/Нет):").strip().lower() == "да":
    char += LOWER_ALPHABET


if input("Включать ли символы? (Да/Нет):").strip().lower() == "да":
    char += PUNCTUATION

if char == "":
    print("В пароле нет никаких символов, попробуй снова")
    exit()


print("\n--- Твои сгенерированные пароли ---")

for i in range(1, counter + 1):
    # Тут твоя функция генерации одного пароля
    password = gen_password(password_len, char)
    print(f"  {i}.  {password}")
