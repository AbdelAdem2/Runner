from djitellopy import Tello
import keyboard

tello = Tello()
tello.connect()
#  L = takeoff
#  C = Land
#  F = Stream on
#  S = Stream off

def on_key_press(key):
    if key.name == "l":
        temp = tello.get_temperature()
        if temp > 30:
            print("Temperature is higher than 30c")
        elif temp < 30:
            print("Temperature is lower than 30c")


keyboard.on_press(on_key_press)
while True:
    pass