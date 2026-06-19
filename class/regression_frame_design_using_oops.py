class TestCase:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(self.name, "executed")

class Regression:
    def __init__(self):
        self.tests = []

    def add_test(self, test):
        self.tests.append(test)

    def run(self):
        for test in self.tests:
            test.execute()

r = Regression()
r.add_test(TestCase("PM Suspend"))
r.add_test(TestCase("DDR Boot"))
r.run()
