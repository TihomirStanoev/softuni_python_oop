from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INSERT_RATE = 1.5
    AMOUNT = 2000.0
    PERCENT = 0.2
    def __init__(self):
        super().__init__(self.INSERT_RATE, self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.PERCENT