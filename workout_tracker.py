#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
from datetime import datetime

APP_ID = ''
API_KEY = ''

GENDER = ''
WEIGHT_KG = ''
HEIGHT_CM = ''
AGE = ''

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = ''

now = datetime.now()
date = now.strftime('%x')
time = now.strftime('%X')
exercise_text = input("Tell me which exercises you did: ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

params = {
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()


for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)