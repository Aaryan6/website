from time import time
# from pygame import mixer
from datetime import datetime
from win32com.client import Dispatch
speak = Dispatch("SAPI.Spvoice")

def musicloop(stopper):
    while True:
        a = input()
        if a == stopper:
            # mixer.audio.stop()

            break
def log_file(msg):
    with open("healthy_programmer.txt","a") as f:
        f.write(f" {msg} {datetime.now()} \n")
init_water = time()
init_eyes = time()
init_ex = time()
water_sec = 5
eyes_sec = 10
ex_sec = 15
while True:
    if time() - init_water > water_sec:
        print("its time drinking water : ")
        print("Type drank to stop task...")
        # musicloop("water.mp3","drank")
        speak.Speak("Drink water")
        init_water = time()
        log_file("Drinking Water : ")

    if time() - init_eyes > eyes_sec:
        print("its time relax your eyes : ")
        print("Type drank to stop task...")
        # musicloop("eyes.mp3","eydone")
        speak.Speak("is time to eyes exercise")
        init_eyes = time()
        log_file("Eyes Exercise : ")

    if time() - init_ex > ex_sec:
        print("its time physical activity : ")
        print("Type drank to stop task...")
        # musicloop("physical.mp3","exdone")
        speak.Speak("is time to physical activity")
        init_ex = time()
        log_file("Physical Activity : ")

