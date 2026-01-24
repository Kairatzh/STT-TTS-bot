from stt.stt import listening
from tts.tts import speak
from instructions import instruction
from prefixes import assistant_prefix, user_prefix

from emotion_app import EmotionViewer 
from intent_emotions import intent
import threading


def main():
    viewer = EmotionViewer()

    viewer_thread = threading.Thread(target=viewer.run, daemon=True)
    viewer_thread.start()

    viewer.set_emotion("happy")
    speak(text="Привет, я Глория, твой ИИ помощник! Задавай вопросы")


    while True:
        command = listening()
        print(f"{user_prefix} {command}")
        emotion = intent(command)
        viewer.set_emotion(emotion)

        response_text = instruction(command)
        print(f"{assistant_prefix} {response_text}")
        
        speak(text=response_text)

        if command == "выход":
            viewer.set_emotion("neutral")
            speak(text="Работа завершена. До свидания.")
            break


if __name__ == "__main__":
    main()
