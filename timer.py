WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

class Timer:

    def __init__(self):
        self.reps = 0
        self.time = 0
        self.mode = None

    def printable_time(self):
        min = self.time // 60
        sec = f'0{self.time % 60}' if self.time % 60 < 10 else f'{self.time % 60}'
        return f'{min}:{sec}'

    def start_timer(self):
        self.reps += 1
        if self.reps % 2 == 1:
            self.time = WORK_MIN*60
            self.mode = 'Work'
        elif self.reps == 8:
            self.time = LONG_BREAK_MIN*60
            self.mode = 'Long Break'
        else:
            self.time = SHORT_BREAK_MIN*60
            self.mode = 'Short Break'

    def reset_timer(self):
        self.reps = 0
        self.time = 0
        self.mode = None

    def decrement(self):
        if self.time >= 0:
            self.time -= 1
        if self.time < 0:
            self.start_timer()