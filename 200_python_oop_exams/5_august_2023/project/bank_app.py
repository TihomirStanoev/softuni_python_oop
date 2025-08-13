from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}
    LOAN_MAPPER = {"StudentLoan": "Student", "MortgageLoan": "Adult"}
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list[BaseLoan] = []
        self.clients: list[BaseClient] = []

    @property
    def granted_sum(self):
        granted = 0
        for client in self.clients:
            for loan in client.loans:
                granted += loan.amount
        return granted
    @property
    def avg_client_interest_rate(self):
        try:
            return sum(c.interest for c in self.clients) / len(self.clients)
        except ZeroDivisionError:
            return 0


    def _find_client_by_id(self, client_id) -> BaseClient | None:
        return next((c for c in self.clients if client_id == c.client_id), None)
    def _find_load_by_type(self, loan_type) -> BaseLoan | None:
        return next((l for l in self.loans if l.loan_type == loan_type), None)

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS.keys():
            raise Exception('Invalid loan type!')
        loan = self.VALID_LOANS[loan_type]()
        self.loans.append(loan)
        return f'{loan_type} was successfully added.'

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS.keys():
            raise Exception('Invalid client type!')
        if len(self.clients) >= self.capacity:
            return 'Not enough bank capacity.'

        client = self.VALID_CLIENTS[client_type](client_name,client_id,income)
        self.clients.append(client)
        return f'{client_type} was successfully added.'

    def grant_loan(self, loan_type: str, client_id: str):
        client = self._find_client_by_id(client_id)
        if self.LOAN_MAPPER[loan_type] != client.client_type:
            raise Exception('Inappropriate loan type!')
        loan = self._find_load_by_type(loan_type)

        self.loans.remove(loan)
        client.loans.append(loan)
        return f'Successfully granted {loan.loan_type} to {client.name} with ID {client.client_id}.'

    def remove_client(self, client_id: str):
        client = self._find_client_by_id(client_id)
        if client is None:
            raise Exception('No such client!')
        if len(client.loans) > 0:
            raise Exception('The client has loans! Removal is impossible!')

        self.clients.remove(client)
        return f'Successfully removed {client.name} with ID {client.client_id}.'

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0
        for loan in self.loans:
            if loan.loan_type == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f'Successfully changed {number_of_changed_loans} loans.'


    def increase_clients_interest(self, min_rate: float):
        clients = list(filter(lambda c: c.interest < min_rate, self.clients))

        for client in clients:
            client.increase_clients_interest()

        return f'Number of clients affected: {len(clients)}.'

    def get_statistics(self):
        result = [
            f'Active Clients: {len(self.clients)}',
            f'Total Income: {sum(c.income for c in self.clients):.2f}',
            f'Granted Loans: {sum(len(c.loans) for c in self.clients)}, Total Sum: {self.granted_sum:.2f}',
            f'Available Loans: {len(self.loans)}, Total Sum: {sum(loan.amount for loan in self.loans):.2f}',
            f'Average Client Interest Rate: {self.avg_client_interest_rate:.2f}'
            ]

        return '\n'.join(result)

