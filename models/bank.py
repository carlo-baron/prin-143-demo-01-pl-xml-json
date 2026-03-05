import py_serializable

@py_serializable.serializable_class
class Bank:
    def __init__(self, *, name: str, transaction: str, amount: str, date: str) -> None:
        self.Name = name
        self.Transaction = transaction
        self.Amount = amount
        self.Date = date

    @property
    def name(self) -> str:
        return self.Name

    @property
    def transaction(self) -> str:
        return self.Name

    @property
    def amount(self) -> str:
        return self.Amount

    @property
    def date(self) -> str:
        return self.Date
