import requests
from datetime import datetime

APP_ID = "5fa17e1e"
API_KEY = "83bb2a7f597ae01dcea740728a9e3810"
GENDER = "FEMALE"
WEIGHT_KG = "80"
HEIGHT = "172.72"
AGE = "41"
sheety_token = "laksfwyr3oiwhrjlksdfnj895y03ur"
sheety_header = {
    "Authorization": "Bearer laksfwyr3oiwhrjlksdfnj895y03ur"
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result)
for exercise in result["exercises"]:
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%X")
    exercise_type = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    post_endpoint = "https://api.sheety.co/78a262a8e64813691484e7fc96e63021/workoutTracking/workouts"

    workout = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise_type,
            "duration": duration,
            "calories": calories,
            }
        }

    response = requests.post(url=post_endpoint, json=workout, headers=sheety_header)
    print(response.text)
