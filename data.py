import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    # "category": 22,
    "difficulty": "easy",
}

results = requests.get("https://opentdb.com/api.php", params=parameters)
results.raise_for_status()
data = results.json()
question_data = data["results"]
