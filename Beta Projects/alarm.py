import datetime as dt
import pygame
import time
# date = dt.date(2025, 1, 20)
# today = dt.datetime.today()
# time = dt.time(7,32)
# now = dt.datetime.now()

# print(date)
# print(today)
# print(time)
# print(now)
# print(now.strftime("%y %m %d"))

# target_dt = dt.datetime(2030,1,23,3,12,33)

def set_alarm():
    alarm_at = input("Enter alarm time in HH:MM:SS format: ")
    print(f"Alarm for {alarm_at} is scheduled sucessfully.")
    my_alarm(alarm_at)

def my_alarm(alarm_at):
    message= input("Enter message here: ")
    current = dt.datetime.now().strftime("%H:%M:%S")
    sound = "alarm-clock-90867.mp3"
    while current < alarm_at :
        current = dt.datetime.now().strftime("%H:%M:%S")
        print(current)
        time.sleep(1)
        if current == alarm_at:
            buzz_alarm(message,sound)
            break


def buzz_alarm(message,sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    print(message)
    
    while pygame.mixer.music.get_busy():
        time.sleep(1)

set_alarm()