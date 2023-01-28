import dictionaries
from dictionaries import zelan_zauz #bakarrik funtzio bat inportarzeko (sakatu contr+space ikusteko aukera guztiak)

class Animal: #clase hau gurasoa da eta besteak honen bitartez definituko dira
    def walk(self):
        print("walk")


class Dog(Animal): #Hemen klasea Animalitik heredatzen ari da
    pass #Bertan pasatzeko esaten diogu lerro hutsik ez egoteko

class Cat(Animal):
    def bark(self):
        print("bark")

dog1 = Dog()

dog1.walk()

dictionaries.probak_dictionaries()

