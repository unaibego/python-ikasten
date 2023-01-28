def probak_dictionaries():
    customer = {"name": "Unai Begoña", "age" : 22} #azken finean lista bat da baina guk jartzen diogu izena indiceari
    print(customer["age"])
    customer["Jaiotze eguna"] = '2000/07/16'
    print(customer["Jaiotze eguna"])
    print(customer.get("hello")) #get jarrita ez bada existitzen none itzuliko digu
    print(customer)


#ariketa
def zenbakiak_idatzi():
    customer = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six"}
    str = input("Enter you phone: ")
    for i in str:
        print(customer.get(i, '!'))

#beste ariketa interesgarri bat
def zelan_zauz():
    message = input("zelan zauz? ")
    words = message.split(' ')
    emojis = {":)": "😀", ":(":"🥺"}
    for word in words:
        print(emojis.get(word, word), " ", end= "") #kasu honetan hitz bakoitza ia indiceen artean dagoen bilatzen du, ez badago hitz berdina itzultzen digu baina aurkitzen badu aldatu egiten du
    print()


def main():
    probak_dictionaries()
    zelan_zauz()


if __name__ == "__main__":
    main()
