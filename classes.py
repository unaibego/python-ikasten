class Point:   #hemen klase bat sortu dugu
    def __init__(self, x, y): #hau konstruktorea da, basikamente deitzerakoan x eta y balioak hasieratu ahalko ditugu
        self.x = x
        self.y = y
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

def no_contstruct():
    point1 = Point() #hemen objetu bat sortu dugu (klase bat hasieratzean)
    point2 = Point() #hainbat objetu desberdin sortu ahal dira klase bakar batetik
    point1.x = 10 #Eta hauek objetuaren atributoak dira, edonon definitu ahal direnak
    point2.x = 1
    point1.y = 20
    print(point1.x)
    print(point2.x)
    point1.draw()


def with_construct():
    point = Point(10,9)
    print(point.x)


def main():
    with_construct()
if __name__ == "__main__":
    main()
