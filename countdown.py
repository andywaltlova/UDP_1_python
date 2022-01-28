import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("Time's up!")

countdown(60)