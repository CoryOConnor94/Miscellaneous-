#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import requests
from datetime import datetime

APP_ID = ''
API_KEY = ''
SHEETY_BEARER = ''

GENDER = ''
WEIGHT_KG = ''
HEIGHT_CM = ''
AGE = ''

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = ''


def get_date_and_time():
    """Returns current date and time formatted"""
    now = datetime.now()
    return now.strftime('%d/%m/%Y'), now.strftime('%X')


def get_exercise_data():
    """Retrieves workout data from Nutritionix API"""
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
    return response.json()


def log_exercise_to_sheety(exercises, date, time):
    """Logs exercise data to google sheet through sheety API"""
    bearer_headers = {
        'Authorization': f'Bearer {SHEETY_BEARER}'
    }
    for exercise in exercises:
        sheet_inputs = {
            "sheet1": {
                "date": date,
                "time": time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=bearer_headers)
        print(sheet_response.text)


def main():
    """Main flow of program"""
    date, time = get_date_and_time()
    exercise_data = get_exercise_data()
    log_exercise_to_sheety(exercise_data['exercises'], date, time)


if __name__ == '__main__':
    main()
