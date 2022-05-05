import speech_recognition 
from pyaudio import PyAudio, paInt16
from vosk import Model, KaldiRecognizer
# to use this things, you need to install pyaudio, vosk and speech_recognition libraries
# also, you need to install "vosk-model-small-ru-0.22" model to recognize speech

'''
Bobylev Yaroslav 2022
This script use pygame library to render the window
'''

class Recognize:
    def __init__(self, path):
        self.micro = PyAudio()

        self.frames_per_buff = 4096

        self.model = Model(path)

        self.rec = KaldiRecognizer(self.model, 16000)

        self.stream = self.micro.open(format=paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=self.frames_per_buff)

    def get_speech(self):

        if self.stream:
            data = self.stream.read(self.frames_per_buff)
            if len(data) == 0:
                quit()
            if self.rec.AcceptWaveform(data):
                self.stream.start_stream()
                recognized_text = eval(self.rec.Result())['text']
                
                return recognized_text

