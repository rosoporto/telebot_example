import os
from mistralai import Mistral
from dotenv import load_dotenv


class MistralJokeGenerator:
    def __init__(self):
        self.api_key = os.getenv('MISTRAL_AI')
        self.model = "mistral-large-2411"
        self.client = Mistral(api_key=self.api_key)

    def generate_joke(self):
        """
        Генерирует шутку дня используя Mistral AI API.

        :return: Шутка дня
        """
        prompt = [
            {"role": "system", "content": "Generate a funny joke for today."},
            {"role": "user", "content": "Tell me a joke."}
        ]
        chat_response = self.client.chat.complete(
            model=self.model,
            messages=prompt
        )
        if chat_response is not None:
            return chat_response.choices.message.content
        else:
            return "Не удалось получить шутку от Mistral AI"

    def generate_joke_with_context(self, context):
        """
        Генерирует шутку дня с учетом контекста используя Mistral AI API.

        :param context: Контекст для шутки
        :return: Шутка дня
        """
        prompt = [
            {"role": "system", "content": "Generate a funny joke for today based on the following context: " + context},
            {"role": "user", "content": "Tell me a joke."}
        ]
        chat_response = self.client.chat.complete(
            model=self.model,
            messages=prompt
        )
        if chat_response is not None:
            return chat_response.choices.message.content
        else:
            return "Не удалось получить шутку от Mistral AI"

# Пример использования класса
if __name__ == "__main__":    
    joke_generator = MistralJokeGenerator()
    joke = joke_generator.generate_joke()
    print("Шутка дня:", joke)

    # Генерация шутки с контекстом
    context = "погода и лето"
    joke_with_context = joke_generator.generate_joke_with_context(context)
    print("Шутка дня с контекстом:", joke_with_context)