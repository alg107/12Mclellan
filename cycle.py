# Have an instance for each cycle and unpickle, advance, display data, repickle
class Cycle:
    def __init__(self, title, names):
        self.title = title
        self.names = names
        self.current_idx = 0

    def current(self):
        return self.names[self.current_idx]

    def advance(self):
        self.current_idx = (self.current_idx+1)%len(names)
        return self.current_idx
