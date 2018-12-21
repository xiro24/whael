import time

class Time:

    def __init__(self):
        self.run = True

    def print_time(self,threadName,delay):
        count =0
        while True:
            time.sleep(delay)
            count+=1
            print("%s: %s" %(threadName, time.ctime(time.time())))
            if self.run == True:
                return