def greetPerson(name):
    if name:
        print(f"Ahoj, {name}!")
    else:
        print("Ahoj, neznámý člověče!")

print(greet_person.__doc__)

greetPerson("John")