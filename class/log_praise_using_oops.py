class LogParser:
    def __init__(self, filename):
        self.filename = filename

    def find_errors(self):
        with open(self.filename, "r") as file:
            for line in file:
                if "ERROR" in line:
                    print(line.strip())

parser = LogParser("log.txt")
parser.find_errors()
