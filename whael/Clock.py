import time as t

class Time:

    def __init__(self):
        self.count = 0
        self.time = 0
        self.seconds = 60
        self.minutes = 60 * self.seconds
        self.hour = 60 * self.minutes
        self.day = 24 * self.hour
        self.week = 7 * self.day
        self.month = 5 * self.week
        self.year = 12 * self.month

    def print_time(self):
        self.count += 1
        if self.count % 28 == 0:
            self.time+=1
            print(self.time)