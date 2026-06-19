class ScoreBoard:
    def __init__(self, score):
        self._score = score

    def get_score(self):
        return self._score


s1 = ScoreBoard(0)

print(s1.get_score())
