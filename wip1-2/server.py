from socket import socket, AF_INET, SOCK_DGRAM
import pyaudio
import wave
import sys

CHUNK = 1024
HOST = ''
PORT = 60000

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, 
                channels=2, 
                rate=44100, 
                output=True,
                frames_per_buffer = CHUNK
                )

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))

sound, address = s.recvfrom(CHUNK*4)

print ('nowplaying from '+ str(address))
while sound != b'':
    stream.write(sound,CHUNK)
    sound, address = s.recvfrom(CHUNK*4)

print('stop')
stream.close()
s.close()
