class Board:
    def __init__(self,name):
        self.name=name
    def start_board(self):
        print(self.name,"board is booting")
    def shutdown(self):
        print(self.name,"shutdown the board")

boot=Board("vck190")  #object creation
boot.start_board()
