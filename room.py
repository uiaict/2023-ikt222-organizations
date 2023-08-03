class Room:
    def __init__(self, name):
        self.name = name
        self.peripherals = {}

    def add_peripheral(self, peripheral):
        self.peripherals[peripheral.name] = peripheral

    def remove_peripheral(self, name):
        del self.peripherals[name]
