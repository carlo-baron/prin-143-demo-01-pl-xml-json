import py_serializable

@py_serializable.serializable_class
class Cinema:
    def __init__(self, *, name: str, open: str, close: str, movie: str) -> None:
        self.Name = name
        self.Open = open
        self.Close = close
        self.Movie = movie

    @property
    def name(self) -> str:
        return self.Name

    @property
    def open(self) -> str:
        return self.Name

    @property
    def close(self) -> str:
        return self.Close

    @property
    def movie(self) -> str:
        return self.Movie
