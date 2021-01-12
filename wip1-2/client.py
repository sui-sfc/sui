import pyaudio
import wave
import time
from socket import socket, AF_INET, SOCK_DGRAM

CHUNK = 1024
filename = "sample.wav"

HOST = ''
PORT = 60000
ADDRESS = '192.168.0.51'

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

empty = b''

for i in range (CHUNK*4):
    empty += b'\x00'

print('Now streaming')
while data != b'':  
    s.sendto(data, (ADDRESS,PORT))
    stream.write(empty,CHUNK)
    data = b''
    data = wf.readframes(CHUNK)
s.close()

stream.stop_stream()
stream.close()
wf.close()
p.terminate()
