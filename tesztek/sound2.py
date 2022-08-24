import matplotlib
matplotlib.use('Agg')
import subprocess
import serial
import alsaaudio
import easygui
import time
import sys
import vlc

vol = input("Üss be egy számot 0-100ig: ")
print("Hangerő: ", vol)

#volume = easygui.integerbox()

m = alsaaudio.Mixer('Master')
current_volume = m.getvolume() 
print('Jelenlegi hangerő: ' % current_volume)
time.sleep(2)
m.setvolume(int(vol))

player = vlc.MediaPlayer("~/Desktop/play.m3u")
print("Ez fut most: ", player)
