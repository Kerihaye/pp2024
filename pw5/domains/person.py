class Person:
    def __init__(self, id, name, date_of_birth):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth

    def display(self):
        raise NotImplementedError("Subclass must implement this method")

