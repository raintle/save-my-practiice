class Employee:

    def __init__(self, first_name, last_name, year_raise):
        self.first_name = first_name
        self.last_name = last_name
        self.year_raise = year_raise

    def give_raise(self, increase=5000):
        self.year_raise += increase