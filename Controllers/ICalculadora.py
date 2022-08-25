from abc import abstractmethod


class ICalculadora:
    def __init__(self):
        pass

    @abstractmethod
    def printOptions(self):
        pass
