# import datetime
# import random
# from data import answers_list, jokes_list, get_weather

# def instructions(command: str):
#     now = datetime.datetime.now()

#     if command in ["привет", "здравствуй", "хай", "hello", "hi", "добрый день", "доброе утро", "добрый вечер"]: text = "Привет! Рад тебя видеть."
#     elif command in ["пока", "до свидания", "бай", "выход", "exit", "увидимся", "прощай"]: text = "До встречи! Хорошего дня."
#     elif command in ["как дела?", "как ты?", "как дела", "что нового", "как настроение"]: text = random.choice(answers_list)
#     elif command in ["который час?", "время", "скажи время", "сколько времени", "время сейчас"]: text = "Текущее время: " + now.strftime("%H:%M:%S")
#     elif command in ["какая сегодня дата?", "дата", "скажи дату", "сегодняшняя дата", "какое сегодня число"]: text = "Сегодняшняя дата: " + now.strftime("%Y-%m-%d")
#     elif command in ["какой сегодня день", "день недели", "что за день"]: text = "Сегодня: " + now.strftime("%A")
#     elif command in ["помоги", "что умеешь", "help", "команды", "список команд"]: text = "Я умею: приветствовать, болтать, шутить, говорить время, дату и погоду."
#     elif command in ["как тебя зовут?", "твое имя", "скажи имя", "кто ты", "как тебя зовут"]: text = "Меня зовут Джастин Бибер."
#     elif command in ["получить погоду", "какая погода?", "погода", "что с погодой"]: text = get_weather()
#     elif command in ["расскажи шутку", "шутка", "смешно", "анекдот", "пошути"]: text = random.choice(jokes_list)
#     elif command in ["ты кто", "что ты такое", "кто ты вообще"]: text = "Я простой голосовой ассистент на Python."
#     elif command in ["спасибо", "благодарю", "thanks", "мерси"]: text = "Пожалуйста! Всегда рад помочь."
#     elif command in ["ты умный", "ты лучший", "ты крутой", "молодец"]: text = "Спасибо, мне приятно это слышать."
#     elif command in ["мне скучно", "скучно", "нечего делать"]: text = "Хочешь шутку или просто поговорим?"
#     elif command in ["что делаешь", "чем занят", "что ты делаешь"]: text = "Жду твоих команд."
#     elif command in ["ты здесь", "ты меня слышишь"]: text = "Да, я здесь."
#     elif command in ["ты живой", "ты настоящий"]: text = "Я не живой, но стараюсь быть полезным."
#     elif command in ["ты робот", "ты бот"]: text = "Да, я бот."
#     elif command in ["да", "ага", "ок", "хорошо"]: text = "Отлично."
#     elif command in ["нет", "неа"]: text = "Хорошо, как скажешь."
#     elif command in ["тест", "проверка", "проверим"]: text = "Тест прошёл успешно."
#     elif command in ["расскажи о себе", "что ты умеешь делать"]: text = "Я голосовой ассистент, созданный для помощи."
#     elif command in ["ты злой", "ты добрый"]: text = "Я всегда настроен дружелюбно."
#     elif command in ["ты устал", "ты не устал"]: text = "Я не устаю."
#     elif command in ["ты меня понимаешь", "ты понял меня"]: text = "Да, я стараюсь понимать тебя."
#     elif command in ["что мне делать", "посоветуй"]: text = "Попробуй задать мне вопрос или попросить помощи."
#     elif command in ["какой сегодня год"]: text = "Сейчас " + now.strftime("%Y") + " год."
#     elif command in ["какой месяц"]: text = "Текущий месяц: " + now.strftime("%B")
#     elif command in ["утро", "день", "вечер", "ночь"]: text = "Надеюсь, у тебя хорошее время суток."
#     elif command in ["ты работаешь", "ты сломался"]: text = "Я работаю корректно."
#     elif command in ["перезапуск"]: text = "Перезапуск не требуется."
#     elif command in ["молчать", "тихо"]: text = "Хорошо, буду ждать."
#     elif command in ["говори"]: text = "Я готов общаться."
#     elif command in ["любишь меня"]: text = "Я здесь, чтобы помогать тебе."
#     elif command in ["что дальше"]: text = "Жду следующую команду."
#     else: text = "Извини, я не понял команду."

#     return text


import random
import datetime
from data import answers_list, jokes_list, get_weather, COMMANDS

def instructions(command: str):
    now = datetime.datetime.now()
    command = command.lower().strip()
    
    for cmd_data in COMMANDS.values():
        if command in cmd_data["keywords"]:
            response = cmd_data["response"]
            
            if response == "random_answer":
                return random.choice(answers_list)
            elif response == "random_joke":
                return random.choice(jokes_list)
            elif response == "time_now":
                return "Текущее время: " + now.strftime("%H:%M:%S")
            elif response == "date_now":
                return "Сегодняшняя дата: " + now.strftime("%Y-%m-%d")
            elif response == "day_now":
                return "Сегодня: " + now.strftime("%A")
            elif response == "year_now":
                return "Сейчас " + now.strftime("%Y") + " год."
            elif response == "month_now":
                return "Текущий месяц: " + now.strftime("%B")
            elif response == "get_weather":
                return get_weather()
            else:
                return response
    
    return "Извини, я не понял команду."