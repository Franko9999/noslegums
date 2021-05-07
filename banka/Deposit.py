class Deposit_class:
    def __init__(self, deposit, term, rate):
        self.deposit = deposit
        self.term = term
        self.rate = rate
        self.deposit_start=deposit


    def interest(self):

        for i in range(0, self.term):
            money = self.deposit + (self.deposit * self.rate+1)
            self.deposit = money
        return money - self.deposit_start