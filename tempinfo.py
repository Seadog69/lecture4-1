import time

class Tempinfo:

    def __init__(self,date,high,low):
        self.date = date
        self.high = high
        self.low = low
    
    def print_info(self):
        print(f"Date: {self.date} High:{self.high} Low:{self.low}")

def main():
    d = time.strftime("%Y%m%d", time.localtime(time.time()))
    t = Tempinfo(date=d, high=81, low=54)
    t.print_info()

if __name__ == "__main__":
    main()