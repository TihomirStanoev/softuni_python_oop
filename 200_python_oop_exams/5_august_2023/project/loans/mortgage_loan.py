from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INSERT_RATE = 3.5
    AMOUNT = 50_000.0
    PERCENT = 0.5
    def __init__(self):
        super().__init__(self.INSERT_RATE, self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.PERCENT