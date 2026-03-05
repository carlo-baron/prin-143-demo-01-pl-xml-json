import py_serializable

@py_serializable.serializable_class
class Politician:
    def __init__(self, *, name: str, age: str, achievement: str) -> None:
        self.Name = name
        self.Age = age
        self.Achievement = achievement

    @property
    def name(self) -> str:
        return self.Name

    @property
    def age(self) -> str:
        return self.Name

    @property
    def achievement(self) -> str:
        return self.Achievement
