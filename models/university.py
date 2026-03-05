import py_serializable

@py_serializable.serializable_class
class University:
    def __init__(self, *, name: str, department: str, student: str) -> None:
        self.Name = name 
        self.Department = department
        self.Student = student

    @property
    def name(self) -> str:
        return self.Name

    @property
    def department(self) -> str:
        return self.Name

    @property
    def student(self) -> str:
        return self.Student
