
import requests
import json
import sys

BASE_URL = "http://localhost:5555"

def test_get_games():
    print(f"Testing GET {BASE_URL}/games...")
    try:
        response = requests.get(f"{BASE_URL}/games")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"Data: {json.dumps(data, indent=2)}")
                return True
            except json.JSONDecodeError:
                print("Response is not valid JSON")
                print(response.text)
                return False
        else:
            print(f"Failed. Response: {response.text}")
            return False
    except requests.exceptions.ConnectionError:
        print("Could not connect to server.")
        return False

def test_get_game_by_id(id):
    print(f"\nTesting GET {BASE_URL}/games/{id}...")
    try:
        response = requests.get(f"{BASE_URL}/games/{id}")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"Data: {json.dumps(data, indent=2)}")
                return True
            except json.JSONDecodeError:
                print("Response is not valid JSON")
                print(response.text)
                return False
        else:
            print(f"Failed. Response: {response.text}")
            return False
    except requests.exceptions.ConnectionError:
        print("Could not connect to server.")
        return False

def test_get_game_users(id):
    print(f"\nTesting GET {BASE_URL}/games/users/{id}...")
    try:
        response = requests.get(f"{BASE_URL}/games/users/{id}")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"Data: {json.dumps(data, indent=2)}")
                return True
            except json.JSONDecodeError:
                print("Response is not valid JSON")
                print(response.text)
                return False
        else:
            print(f"Failed. Response: {response.text}")
            return False
    except requests.exceptions.ConnectionError:
        print("Could not connect to server.")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "games":
            test_get_games()
        elif command == "game_id":
            test_get_game_by_id(1)
        elif command == "users":
            test_get_game_users(1)
        else:
            print("Unknown command. Usage: python verify_api.py [games|game_id|users]")
            # Run all if no specific command
            test_get_games()
            test_get_game_by_id(1)
            test_get_game_users(1)
    else:
        test_get_games()
        test_get_game_by_id(1)
        test_get_game_users(1)
