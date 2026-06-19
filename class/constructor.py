'''class Test:

    def __init__(self):
        print("Constructor Called")

obj = Test()'''

class Board:
    def __init__(self, name):
        self.name = name
    def boot(self):
        print("Booting Linux")
    def shutdown(self):
        print("Power Off")
board = Board()
board.boot()
