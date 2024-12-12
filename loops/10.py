### Make This System 
import time 
max_attemps = 5
attempt_no = 1
waiting_time = 1

while attempt_no <= max_attemps : 
    print("The Attempt No is -> ", attempt_no, "The Waiting time is Currently is -> ", waiting_time)
    time.sleep(waiting_time)
    attempt_no += 1
    waiting_time *= 2
    