import requests


def get_joke(joke_type):
    """
    Функция для получения шутки с API jokeapi.dev.

    :param joke_type: Тип шутки ('single' или 'twopart').
    :return: Данные шутки в формате JSON или сообщение об ошибке.
    """
    url = "https://v2.jokeapi.dev/joke/Programming"
    params = {
        "type": joke_type,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Проверка на ошибки HTTP
        json_data = response.json()
        if json_data.get("error"):
            return "Error: Unable to retrieve joke."
        return json_data
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


def get_joke_single(joke_type="single"):
    """
    Функция для получения однострочной шутки.

    :param joke_type: Тип шутки (по умолчанию 'single').
    :return: Текст шутки или сообщение об ошибке.
    """
    result = get_joke(joke_type)
    if isinstance(result, dict) and "joke" in result:
        return result["joke"]
    return result


def get_joke_twopart(joke_type="twopart"):
    """
    Функция для получения двухчастной шутки.

    :param joke_type: Тип шутки (по умолчанию 'twopart').
    :return: Кортеж с частью шутки и её продолжением или сообщение об ошибке.
    """
    result = get_joke(joke_type)
    if isinstance(result, dict) and "setup" in result and "delivery" in result:
        return result["setup"], result["delivery"]
    return result


if __name__ == '__main__':
    # Пример использования функции для получения однострочной шутки
    result_single = get_joke_single("single")
    print("Single Joke:", result_single)

    # Пример использования функции для получения двухчастной шутки
    result_twopart = get_joke_twopart("twopart")
    print("Two-part Joke:", result_twopart)