def coffee_quiz():
    print("Vítejte v dotazníku: Jaký druh kávy jste?")
    print("Odpovězte na následující otázky, abychom vám řekli, jaký druh kávy vás nejlépe reprezentuje.")

    name = input("Jak se jmenujete? ")
    age = input("Kolik vám je let? ")
    coffee_preference = input("Máte rádi kávu? (Ano/Ne) ").lower()

    if coffee_preference == "ano":
        print(f"Děkuji, {name}! Jste určitě skvělým příznivcem kávy.")
        print("Máte rádi espresso, cappuccino nebo latte?")

        coffee_choice = input("Vyberte svůj oblíbený druh kávy: ")

        if "espresso" in coffee_choice:
            print(f"{name}, jste jako espresso - silný a energický!")
        elif "cappuccino" in coffee_choice:
            print(f"{name}, jste jako cappuccino - lehký a pěnivý!")
        elif "latte" in coffee_choice:
            print(f"{name}, jste jako latte - hladký a jemný!")
        else:
            print(f"{name}, vaše kávová preference je nejasná, ale to je taky v pořádku!")

    else:
        print(f"{name}, nejste fanouškem kávy? To je v pořádku, taky existuje spousta jiných nápojů!")


coffee_quiz()