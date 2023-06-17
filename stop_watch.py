import time

class Input:
    def start(self):
        self.start_text = input('Please enter 1 to start ')
        self.start_time = time.time()
        
    def split(self):
        self.split_text = input('Please enter 2 to split ')
        self.split_time = time.time()
    
    def stop(self):
        self.stop_text = input('Please enter 3 to stop ')
        self.stop_time = time.time()

class Time_diff:
    def diff(self, start, end):
        diff_time = end - start
        diff_env.conversion(diff_time)
    
    def conversion(self, diff_time):
        hour = diff_time / 60 / 60
        minute = diff_time / 60 % 60
        second = diff_time % 60
        milli_second = (second - int(second)) * 1000
        print(str(int(hour)) + ":" + str(int(minute)) + ":" + str(int(second)) + "." +str(int(milli_second)))

if __name__ == '__main__':
    time_env = Input()
    time_env.start()
    time_env.split()
    time_env.stop()
    diff_env = Time_diff()
    print("ラップ1")
    diff_env.diff(time_env.start_time, time_env.split_time)
    print("ラップ2")
    diff_env.diff(time_env.split_time, time_env.stop_time)
    print("タイム")
    diff_env.diff(time_env.start_time, time_env.stop_time)