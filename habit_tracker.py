import requests
from datetime import datetime

USERNAME = 'fitmitch1'      # Validation rule: [a-z][a-z0-9-]{1,32}
TOKEN = ''      # Validation rule: [ -~]{8,128}
headers = {
    'X-USER-TOKEN': TOKEN
}
GRAPH_ID = "graph1"     # Validation rule: ^[a-z][a-z0-9-]{1,16}
pixela_endpoint = 'https://pixe.la/v1/users'
today = datetime.today().strftime('%Y%m%d')


def create_user():
    """Creates pixela user with user created token and username"""
    params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=pixela_endpoint, json=params)
    print(response.text)


def create_graph():
    """Creates pixela graph"""
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

    graph_config = {
        "id": "graph1",
        "name": "Jogging Graph",
        "unit": "Km",
        "type": "float",
        "color": "shibafu",
    }

    requests.post(url=graph_endpoint, json=graph_config, headers=headers)


def add_pixel():
    """Adds pixel habit entry to graph"""
    pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": today,
        "quantity": input("How many Km did you run today? "),
    }

    response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
    print(response.text)


def main():
    """Main flow of program"""
    # create_user()     # Uncomment to create new user
    # create_graph()    # Uncomment to create new graph
    add_pixel()


if __name__=='__main__':
    main()
