import json
import pyaudio
from vosk import Model, KaldiRecognizer

class STT:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.model = Model("C:/Users/User/Desktop/STT_TTS/listen_model/model_small")
        self.recognizer = KaldiRecognizer(self.model, 16000)

        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=8000
        )

    def listen(self) -> str:
        self.stream.start_stream()

        while True:
            data = self.stream.read(8000, exception_on_overflow=False)
            if self.recognizer.AcceptWaveform(data):
                result = json.loads(self.recognizer.Result())
                text = result.get("text", "").strip()
                if text:
                    return text.lower()

stt = STT()

def listening() -> str:
    text = stt.listen()
    return text.lower().strip()