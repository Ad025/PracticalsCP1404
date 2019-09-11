class user:
    def __init__(self, name, number_of_tacos, score):
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

    def __str__(self):
        return "{},{},{}".format(self.name, self.number_of_tacos, self.score)



p1 = user("jim", 2, 4)
print(p1)
