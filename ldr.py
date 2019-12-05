from gpiozero import LightSensor, Buzzer, Button
from time import sleep
import pygame.mixer
from pygame.mixer import Sound

pygame.mixer.init()

ldr = LightSensor(4)
buzzer= Buzzer(17)
frank = Sound('/home/pi/Downloads/bing-bing-walla-walla.wav')
button = Button(21)

while True:
    sleep(0.1)
    if ldr.value < 0.5:
        buzzer.on()
        frank.play()
    else:
        buzzer.off()
        frank.stop()

while True:
   if button.wait_for_press():
       Program.restart()
    else print("Armed"):
    
    




