import pickle
from datetime import datetime

# Have an instance for each cycle and unpickle, advance, display data, repickle
class Cycle:
    def __init__(self, title, names, identifier=None):
        self.title = title
        if identifier:
            self.identifier = identifier
        else:
            self.identifier = abs(hash(title))

        self.names = names
        self.current_idx = 0
        self.save()

    def current(self):
        return self.names[self.current_idx]

    def advance(self):
        self.current_idx = (self.current_idx+1)%len(self.names)
        return self.current_idx

    def save(self):
        pickle.dump(self, open("db/"+self.identifier+".p", "wb"))

    @staticmethod
    def load(fname):
        return pickle.load(open('db/'+fname+".p", "rb"))

    @staticmethod
    def easy_save(obj, fname):
        pickle.dump(obj, open("db/"+fname+".p", "wb"))


class Notice:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.time = datetime.now()
        self.identifier = abs(hash(self.time))
        print(self.time)

    @staticmethod
    def save_list(lst, fname):
        pickle.dump(lst, open("db/"+fname+".p", "wb"))

    @staticmethod
    def load_list(fname):
        return pickle.load(open('db/'+fname+".p", "rb"))
