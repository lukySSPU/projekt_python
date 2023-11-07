import random
import string

def convert_czech_date_to_database_format(czech_date):
    day, month, year = czech_date.split('. ')
    database_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    return database_date

def convert_phrase_to_identifiers(phrase, snake_case=True, camel_case=False):
    words = phrase.split()
    if snake_case:
        identifier = "_".join(words).lower()
    elif camel_case:
        identifier = "".join(word.capitalize() for word in words)
    return identifier

def generate_random_passwords(num_passwords):
    passwords = []
    for _ in range(num_passwords):
        uppercase = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        lowercase = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
        special_char = random.choice("-/+*")
        digits = ''.join(random.choice(string.digits) for _ in range(3))
        password = uppercase + lowercase + special_char + digits
        passwords.append(password)
    return passwords

# Příklad použití

# 1. Převod data
czech_date = "12. 10. 2020"
database_date = convert_czech_date_to_database_format(czech_date)
print(f"Databázové datum: {database_date}")

# 2. identifikatory
python_phrase = "To je proměnná v Pythonu"
python_identifier = convert_phrase_to_identifiers(python_phrase)
print(f"Python identifikátor: {python_identifier}")

js_phrase = "To je proměnná v Pythonu"
js_identifier = convert_phrase_to_identifiers(js_phrase, snake_case=False)
print(f"JavaScript camel case: {js_identifier}")

# 3. Generování hesel
num_passwords = 5
random_passwords = generate_random_passwords(num_passwords)
print("Náhodná hesla:")
for password in random_passwords:
    print(password)
