import py_serializable

@py_serializable.serializable_class
class Retail:
    def __init__(self, *, store: str, address: str, section: str, product: str) -> None:
        self.Store = store
        self.Address = address
        self.Section = section
        self.Product = product

    @property
    def store(self) -> str:
        return self.Store

    @property
    def address(self) -> str:
        return self.Store

    @property
    def section(self) -> str:
        return self.Section

    @property
    def product(self) -> str:
        return self.Product
