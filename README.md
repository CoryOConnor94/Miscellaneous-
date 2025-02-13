# Miscellaneous Repository

This repository contains various scripts, including a Habit Tracker using Pixela.

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

## Features

## Prerequisites

## Setup

## Usage

## Configuration

## Example Output

## Notes

## Resources

## License
This project is licensed under the MIT License.

