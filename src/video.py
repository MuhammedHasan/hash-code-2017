class Video:

    def __init__(self, id, size):
        self.id = id
        self.size = size

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id
