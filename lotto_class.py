import random

class number:

    def __init__(self):
        self.lotto_number = []

    def random_machine(self):
        random_set = []
        for i in range(0, 7):
            self.lotto_number.append(random.randint(1, 46))
        random_set = set(self.lotto_number)
        return self.lotto_number

round_1 = number()


print(round_1.random_machine())