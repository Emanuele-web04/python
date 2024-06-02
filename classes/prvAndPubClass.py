# Private means that is accessible within something, like a file
# and so it's not accessible between outside files

# The opposite with public, other classes can modify the class, unless it's defined as final

# just a convention
class _Private:
    def __init__(self, name) -> None:
        self.name = name

class NotPrivate:
    def __init__(self, name) -> None:
        self.name = name
        self.priv = _Private(name)
    
    def _display(self):
        print("hello")

    def display(self):
        print("hello")