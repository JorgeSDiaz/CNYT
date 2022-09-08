from abc import abstractmethod


class IComplejo:
    def __init__(self):
        pass

    @abstractmethod
    def get(self) -> str:
        pass

    @staticmethod
    @abstractmethod
    def decode(item: str):
        pass

    @staticmethod
    @abstractmethod
    def recibaNum():
        pass

