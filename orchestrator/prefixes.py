class Prefixes:
    @staticmethod
    def AssistantPrefix():
        return "Assistant: "
    @staticmethod
    def UserPrefix():
        return "You: "

user_prefix = Prefixes.UserPrefix()
assistant_prefix = Prefixes.AssistantPrefix()