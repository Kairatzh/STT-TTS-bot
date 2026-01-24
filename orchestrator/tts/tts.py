from silero_tts.silero_tts import SileroTTS
import pygame
import os
import time

pygame.init()

class TTS:
    def __init__(self):
        self.voice_assistant = SileroTTS(
            model_id="v4_ru",
            language='ru',
            speaker='baya'
        )
    def say(self, text: str):
        file_name = "output.wav"
        self.voice_assistant.tts(text, file_name)
        time.sleep(0.1)
        self.play_music(file_name)

    def play_music(self, file_name):
        try:
            pygame.mixer.quit()
            pygame.mixer.init(frequency=24000)
            pygame.mixer.music.load(file_name)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            pygame.mixer.quit()
            os.remove(file_name)
        except Exception as e:
            print(f'Ошибка воспроизведения: {e}')

tts_engine = TTS()


def speak(text: str):
    tts_engine.say(text)
