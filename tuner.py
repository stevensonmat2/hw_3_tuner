import numpy as np
import pyaudio
from scipy import signal
from scipy.io import wavfile
import sys

# source: https://github.com/mzucker/python-tuner/blob/master/tuner.py

SAMPLES = 48000
FRAME_SIZE = 8192
FRAMES_PER_FFT = 16
SAMPLES_PER_FFT = FRAME_SIZE * FRAMES_PER_FFT
FREQ_STEP = float(SAMPLES) / SAMPLES_PER_FFT

window = signal.windows.triang(SAMPLES_PER_FFT)

if len(sys.argv) > 1:
    file = sys.argv[1]
    _, data = wavfile.read(file)
    data = data[:len(window)]

    if len(data) < len(window):
        padded = np.zeros(SAMPLES_PER_FFT, dtype=np.float32)
        padded[-len(data):] = data
        data = padded

    fft = np.fft.rfft(window * data)
    frequency = np.abs(fft.argmax()) * FREQ_STEP

    print(frequency)

else:

    stream = pyaudio.PyAudio().open(
        format=pyaudio.paInt16,
        channels=1,
        rate=SAMPLES,
        input=True,
        frames_per_buffer=FRAME_SIZE,
    )

    stream.start_stream()
    buffer = np.zeros(SAMPLES_PER_FFT, dtype=np.float32)

    while stream.is_active():
        buffer[-FRAME_SIZE:] = np.frombuffer(stream.read(FRAME_SIZE), np.int16)
        fft = np.fft.rfft(window * buffer)
        frequency = np.abs(fft.argmax()) * FREQ_STEP

        print(frequency)