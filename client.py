import pyaudio
import wave
import time
from socket import socket, AF_INET, SOCK_DGRAM

CHUNK = 1024
filename = "sample.wav"

HOST = ''
PORT = 60000
ADDRESS = 'server ip adress'

s = socket(AF_INET, SOCK_DGRAM)

wf = wave.open(filename, 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=2,
                rate=44100,
                output=True,
                frames_per_buffer = CHUNK
                )
data = wf.readframes(CHUNK)

print('Now streaming')

while data != '':  
    s.sendto(data, (ADDRESS,PORT))
    stream.write(data , CHUNK)
    data = wf.readframes(CHUNK)

s.close()
stream.stop_stream()
stream.close()

p.terminate()
