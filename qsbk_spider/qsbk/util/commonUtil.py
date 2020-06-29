class IteratorAsList(list):
    def __init__(self, it):
        self.it = it
    def __iter__(self):
        return self.it
    def __len__(self):
        return 1