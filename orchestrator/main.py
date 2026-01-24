from stt.stt import listening
from tts.tts import speak
from instructions import instructions
from prefixes import assistant_prefix, user_prefix


def main():
    speak(text="Искусственный интеллект запущен и готов к работе.")

    while True:
        command = listening()
        print(f"{user_prefix} {command}")

        response = instructions(command)
        print(f"{assistant_prefix} {response}")

        speak(text=response)

        if command == "выход":
            speak(text="Работа завершена. До свидания.")
            break


if __name__ == "__main__":
    main()
