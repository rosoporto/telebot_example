import requests


def get_joke(joke_type):
    url = "https://v2.jokeapi.dev/joke/Programming"
    params = {
        "type": joke_type,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    json_data = response.json()
    if json_data.get("error"):
        return "Error"
    return json_data
    

def get_joke_single(joke_type="single"):
    result = get_joke(joke_type)
    return result["joke"]


def get_joke_twopart(joke_type="twopart"):
    result = get_joke(joke_type)
    return result["setup"], result["delivery"]


if __name__ == '__main__':
    result = get_joke()
    print(result)