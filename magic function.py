class book:
    def __init__(self, name, artist, cost):
        self.name = name
        self.artist = artist
        self.cost = cost

    def __eq__(self, other):
        return self.cost == other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def __ge__(self, other):
        return self.cost >= other.cost

book1 = book("abc", "xyz", 420)
book2 = book("def", "mno", 420)
print("The cost of the book1 and the cost of the book2 is equal: ",book1 == book2)
print("The cost of the book1 is lesser than or equal to the cost of the book2: ",book1 <= book2)
print("The cost of the book1 is greater than or equal to the cost of the book2: ",book1 >= book2)