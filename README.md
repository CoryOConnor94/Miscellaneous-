# Miscellaneous Repository

This repository contains various scripts, including a Habit Tracker using Pixela

## Habit Tracker

The Habit Tracker script interacts with the Pixela API to track habits by logging daily progress to a graph. It allows users to:
- Create a Pixela user account directly in the script
- Create a habit tracking graph
- Add daily progress to the graph

## Features
- **User Creation**: Registers a new user on Pixela (only needed once).
- **Graph Creation**: Creates a habit tracking graph (only needed once per habit).
- **Log Progress**: Adds a daily habit entry to the graph.

## Prerequisites
- Python 3.x installed
- `requests` library installed (`pip install requests`)

## Setup
1. Clone this repository or download the script.
2. Install required dependencies (if not already installed):
   ```sh
   pip install requests
   ```
3. The script will prompt you to create a Pixela account if one does not exist.
4. The `USERNAME`, `TOKEN`, and GRAPH_ID values follow specific validation rules, which are commented in the script:
   ```python
   USERNAME = 'your_username'  # Must start with a letter and be 2-32 characters long, lowercase only
   TOKEN = 'your_token'  # Must be 8-128 characters long with any printable ASCII character
   GRAPH_ID = 'your_graphID'  # Must start with a letter and be 2-16 characters long, lowercase only
   ```

## Usage

### 1. Create a Pixela User (First-Time Setup Only)
Uncomment the `create_user()` function call in `main()` and run:
```sh
python habit_tracker.py
```
Once the user is created successfully, you can comment this line again.

### 2. Create a Habit Graph (First-Time Setup Only)
Uncomment the `create_graph()` function call in `main()` and run:
```sh
python habit_tracker.py
```
Once the graph is created successfully, comment this line again.

### 3. Log a Daily Entry
Simply run the script:
```sh
python habit_tracker.py
```
You will be prompted to enter your daily progress.

## Configuration
Modify these parameters in the script as needed:
- `GRAPH_ID`: Change to match different habit tracking graphs.
- `color`: Change the graph color (`shibafu`, `momiji`, `sora`, `ichou`, `ajisai`).
- `unit`: Change to match the type of habit being tracked (e.g., `Hours`, `Pages`).

## Example Output
```
How many Km did you run today? 5
{"message":"Success.","isSuccess":true}
```

## Notes
- User and graph creation should only be run **once**.
- Once set up, only the `add_pixel()` function is needed to log daily progress.

## Resources
- Pixela API Documentation: [https://docs.pixe.la/](https://docs.pixe.la/)

-------------------------------------------------------------------------------

## Workout Tracker

This script allows users to track their workouts by logging exercise data into a Google Sheet using the Sheety API. It utilizes the Nutritionix API to process natural language input and extract workout details such as exercise name, duration, and calories burned.

## Features
- **Automatic Exercise Recognition**: Uses the Nutritionix API to interpret user input.
- **Google Sheet Logging**: Saves exercise details to a Google Sheet via Sheety API.
- **Timestamps**: Automatically records the date and time of workouts.

## Prerequisites
- Python 3.x installed
- `requests` library installed (`pip install requests`)
- Accounts and credentials for:
  - [Nutritionix API](https://www.nutritionix.com/business/api)
  - [Sheety API](https://sheety.co/)

## Setup
1. Clone this repository or download the script.
2. Install required dependencies:
   ```sh
   pip install requests
   ```
3. Set up your API credentials by replacing the placeholder values in the script:
   ```python
   APP_ID = 'your_nutritionix_app_id'
   API_KEY = 'your_nutritionix_api_key'
   SHEETY_BEARER = 'your_sheety_bearer_token'
   SHEETY_ENDPOINT = 'your_sheety_api_endpoint'
   ```
4. Provide personal details for accurate tracking:
   ```python
   GENDER = 'your_gender'
   WEIGHT_KG = 'your_weight'
   HEIGHT_CM = 'your_height'
   AGE = 'your_age'
   ```

## Usage
1. Run the script:
   ```sh
   python workout_tracker.py
   ```
2. Enter your workout details when prompted:
   ```
   Tell me which exercises you did: ran 5km and did 30 push-ups
   ```
3. The script will process the input and log it into your Google Sheet.

## Example Output
```
Tell me which exercises you did: ran 5km
{"message":"Success.","isSuccess":true}
```

## Notes
- Ensure that your Sheety project is configured to accept POST requests.
- You can modify the script to store additional workout details.

## Resources
- [Nutritionix API Documentation](https://www.nutritionix.com/business/api)
- [Sheety API Documentation](https://sheety.co/)

## License
This project is licensed under the MIT License.
